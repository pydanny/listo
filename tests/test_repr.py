import pytest

from listo import listo


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], "0 items: []"),
        ([1], "1 items: [1]"),
        ([1, 2, 3], "3 items: [1, 2, 3]"),
        ([0, 1, 2, 3, 4, 5], "6 items: [0, 1, 2, 3, 4, 5]"),
        ([0, 1, 2, 3, 4, 5, 6], "7 items: ([0, 1, 2, 3, 4], Ellipsis, 6)"),
    ],
)
def test_repr_displays_contents_without_recursing(values, expected):
    assert repr(listo(values)) == expected


def test_repr_of_nested_listo():
    assert repr(listo([listo(1, 2), "three"])) == "2 items: [2 items: [1, 2], 'three']"


def test_string_conversion_uses_safe_representation():
    assert str(listo(1, 2, 3)) == "3 items: [1, 2, 3]"


def test_repr_of_recursive_listo():
    values = listo()
    values.append(values)
    assert repr(values) == "1 items: [...]"


def test_repr_of_long_recursive_listo():
    values = listo(range(6))
    values.append(values)
    assert repr(values) == "7 items: ([0, 1, 2, 3, 4], Ellipsis, ...)"
