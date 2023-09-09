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
