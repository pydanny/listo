from listo import listo


def test_first():
    lst = listo(1, 2, 3, 4)
    assert lst.first() == 1


def test_last():
    lst = listo(1, 2, 3, 4)
    assert lst.last() == 4


def test_min():
    lst = listo(1, 2, 3, 4)
    assert lst.min() == 1


def test_max():
    lst = listo(1, 2, 3, 4)
    assert lst.max() == 4


def test_median():
    lst = listo(1, 2, 3, 4)
    assert lst.median() == 3


def test_join():
    lst = listo(1, 2, 3, 4)
    assert lst.join("-") == "1-2-3-4"


def test_shuffle():
    lst = listo(range(100))
    assert lst.shuffle() != lst


def test_type():
    lst = listo(1, 2, 3, 4)
    assert isinstance(lst, list)
    assert isinstance(lst, listo)


def test_unpacking_of_single_list_arg():
    lst = listo([1, 2, 3, 4])
    assert lst == [1, 2, 3, 4]


def test_unpacking_of_single_tuple_arg():
    lst = listo((1, 2, 3, 4))
    assert lst == [1, 2, 3, 4]


def test_assignment_of_multiple_iterator_args():
    lst = listo([1, 2, 3], (4, 5, 6))
    assert lst == [[1, 2, 3], (4, 5, 6)]


def test_len():
    lst = listo(1, 2, 3, 4)
    assert lst.len() == 4


def test_reverse():
    lst = listo(range(10))
    assert lst.reverse() == list(range(9, -1, -1))


def test_random_choice():
    lst = listo(range(10))
    assert lst.random_choice() in lst


def test_map():
    lst = listo(["a", "b", "c"])
    assert lst.map(lambda x: x.upper()) == ["A", "B", "C"]


def test_filter():
    lst = listo(range(10))
    assert lst.filter(lambda x: x % 3) == [1, 2, 4, 5, 7, 8]


def test_unique():
    lst = listo(1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
    assert lst.unique() == [1, 2, 3, 4]


def test_sorted_returns_new_listo():
    lst = listo(3, 1, 2)
    result = lst.sorted()
    assert isinstance(result, listo)
    assert result == [1, 2, 3]
    assert lst == [3, 1, 2]


def test_sorted_with_key_and_reverse():
    lst = listo("aa", "b", "ccc")
    result = lst.sorted(key=len, reverse=True)
    assert result == ["ccc", "aa", "b"]


def test_sort_returns_new_listo():
    lst = listo(3, 1, 2)
    result = lst.sort()
    assert isinstance(result, listo)
    assert result == [1, 2, 3]
    assert lst == [3, 1, 2]


# def test_repr():
#     lst = list(range(6))
#     assert lst.__repr__() == "[0, 1, 2, 3, 4, 5]"
#     lst = list(range(7))
#     assert lst.__repr__() == [0, 1, 2, 3, 4, 5]
