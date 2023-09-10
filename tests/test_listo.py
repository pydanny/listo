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
    lst = listo(1, 2, 3, 4)
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
