"""Live-length regressions that must preserve PR48's safe representation."""

import unittest

from listo import listo


class LiveLengthRepresentationTests(unittest.TestCase):
    def test_len_tracks_inherited_mutations_after_a_read(self):
        cases = [
            ("append", lambda x: x.append(4), [1, 2, 3, 4]),
            ("extend", lambda x: x.extend([4, 5]), [1, 2, 3, 4, 5]),
            ("insert", lambda x: x.insert(0, 0), [0, 1, 2, 3]),
            ("pop", lambda x: x.pop(), [1, 2]),
            ("remove", lambda x: x.remove(2), [1, 3]),
            ("clear", lambda x: x.clear(), []),
            (
                "replace_slice",
                lambda x: x.__setitem__(slice(1, 2), [4, 5]),
                [1, 4, 5, 3],
            ),
            ("delete_slice", lambda x: x.__delitem__(slice(1, None)), [1]),
            ("iadd", lambda x: x.__iadd__([4]), [1, 2, 3, 4]),
            ("imul", lambda x: x.__imul__(2), [1, 2, 3, 1, 2, 3]),
            ("imul_zero", lambda x: x.__imul__(0), []),
            ("replace_item", lambda x: x.__setitem__(1, 9), [1, 9, 3]),
        ]
        for name, mutate, expected in cases:
            with self.subTest(mutation=name):
                values = listo(1, 2, 3)
                self.assertEqual(values.len(), 3)
                mutate(values)
                self.assertEqual(list(values), expected)
                self.assertEqual(values.len(), len(expected))
                self.assertEqual(values.len(), len(values))

    def test_each_read_sees_subsequent_growth_and_clear(self):
        values = listo()
        self.assertEqual(values.len(), 0)
        values.append(1)
        self.assertEqual(values.len(), 1)
        values.extend([2, 3])
        self.assertEqual(values.len(), 3)
        values.clear()
        self.assertEqual(values.len(), 0)

    def test_median_uses_current_size_without_changing_rounding(self):
        cases = [
            ([10, 20], lambda x: x.append(30), 20),
            ([10, 20, 30, 40], lambda x: x.pop(), 20),
            ([10, 20, 30, 40, 50], lambda x: x.__delitem__(slice(2, None)), 10),
            ([10, 20, 30, 40], lambda x: None, 30),
            ([10, 20, 30, 40, 50, 60], lambda x: None, 30),
        ]
        for initial, mutate, expected in cases:
            with self.subTest(initial=initial, expected=expected):
                values = listo(initial)
                values.median()
                mutate(values)
                before = list(values)
                self.assertEqual(values.median(), expected)
                self.assertEqual(list(values), before)

    def test_median_of_cleared_list_retains_index_error(self):
        values = listo(10, 20, 30)
        values.median()
        values.clear()
        with self.assertRaises(IndexError):
            values.median()

    def test_shuffle_samples_current_multiset_without_mutation(self):
        cases = [
            ("grow", lambda x: x.append(2), [1, 1, 2, 2]),
            ("shrink", lambda x: x.pop(), [1, 1]),
            ("clear", lambda x: x.clear(), []),
            ("unchanged", lambda x: None, [1, 1, 2]),
        ]
        for name, mutate, expected in cases:
            with self.subTest(mutation=name):
                values = listo(1, 1, 2)
                values.shuffle()
                mutate(values)
                self.assertCountEqual(values.shuffle(), expected)
                self.assertEqual(list(values), expected)

    def test_repr_uses_live_count_and_correct_short_long_branch(self):
        cases = [
            (list(range(7)), lambda x: x.pop(), "6 items: [0, 1, 2, 3, 4, 5]"),
            (list(range(7)), lambda x: x.clear(), "0 items: []"),
            (
                [],
                lambda x: x.extend(range(7)),
                "7 items: ([0, 1, 2, 3, 4], Ellipsis, 6)",
            ),
            (
                list(range(7)),
                lambda x: x.append(7),
                "8 items: ([0, 1, 2, 3, 4], Ellipsis, 7)",
            ),
            (list(range(6)), lambda x: None, "6 items: [0, 1, 2, 3, 4, 5]"),
            (list(range(7)), lambda x: None, "7 items: ([0, 1, 2, 3, 4], Ellipsis, 6)"),
        ]
        for initial, mutate, expected in cases:
            with self.subTest(initial_size=len(initial), expected=expected):
                values = listo(initial)
                values.len()
                mutate(values)
                before = list(values)
                self.assertEqual(repr(values), expected)
                self.assertEqual(str(values), expected)
                self.assertEqual(list(values), before)

    def test_short_self_reference_after_cached_empty_read(self):
        values = listo()
        self.assertEqual(values.len(), 0)
        values.append(values)
        self.assertEqual(repr(values), "1 items: [...]")
        self.assertEqual(len(values), 1)
        self.assertIs(values[0], values)

    def test_long_self_reference_after_cached_six_read(self):
        values = listo(range(6))
        self.assertEqual(values.len(), 6)
        values.append(values)
        self.assertEqual(repr(values), "7 items: ([0, 1, 2, 3, 4], Ellipsis, ...)")
        self.assertEqual(len(values), 7)
        self.assertIs(values[-1], values)

    def test_nested_repr_retains_inner_recursion_guard(self):
        inner = listo()
        inner.append(inner)
        outer = listo([inner, "three"])
        self.assertEqual(repr(outer), "2 items: [1 items: [...], 'three']")
        self.assertIs(outer[0], inner)

    def test_len_median_and_repr_do_not_iterate_contents(self):
        class CountingListo(listo):
            def __iter__(self):
                self.iterations += 1
                return super().__iter__()

        values = CountingListo(10, 20)
        values.iterations = 0
        self.assertEqual(values.len(), 2)
        values.append(30)
        self.assertEqual(values.len(), 3)
        self.assertEqual(values.median(), 20)
        self.assertEqual(repr(values), "3 items: [10, 20, 30]")
        self.assertEqual(values.iterations, 0)
        self.assertEqual(list.__getitem__(values, slice(None)), [10, 20, 30])

    def test_reordering_preserves_length_and_existing_return_behavior(self):
        values = listo(3, 1, 2)
        self.assertEqual(values.len(), 3)
        self.assertEqual(values.reverse(), [2, 1, 3])
        self.assertEqual(values.sort(), [1, 2, 3])
        self.assertEqual(list(values), [3, 1, 2])
        list.reverse(values)
        self.assertEqual(values.len(), 3)
        self.assertEqual(list(values), [2, 1, 3])
        list.sort(values)
        self.assertEqual(values.len(), 3)
        self.assertEqual(list(values), [1, 2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
