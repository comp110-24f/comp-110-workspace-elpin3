from CQs.cq07.find_max import find_and_remove_max

"""CQ07 Max Test for Find Max"""

__author__ = "730768189"


def test_expected_find_and_remove_max() -> None:
    ls = [1, 2, 3, 5, 6]
    assert find_and_remove_max(ls) == 6


def test_mutates_find_and_remove_max() -> None:
    ls = [3, 2, 1, 2, 3]
    find_and_remove_max(ls)
    assert ls == [2, 1, 2]


def test_edge_find_and_remove_max() -> None:
    ls = []
    assert find_and_remove_max(ls) == -1
