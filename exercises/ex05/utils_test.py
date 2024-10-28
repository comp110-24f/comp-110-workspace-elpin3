from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""Utils test"""

__author__ = "730768189"


# only_evens tests
def test_1use_only_evens() -> None:
    """Tests use case for only_evens"""
    ls = [1, 2, 3, 4, 5, 6]
    assert only_evens(ls) == [2, 4, 6]


def test_2use_only_evens() -> None:
    """Tests use case for only_evens"""
    ls = [-6, -5, -4, -3, -2, -1]
    assert only_evens(ls) == [-6, -4, -2]


def test_3edge_only_evens() -> None:
    """Tests edge case for only_evens"""
    ls = [-1, -1, -1, -1, -1]
    assert only_evens(ls) == []


# sub tests
def test_1edge_sub() -> None:
    """Tests edge case for sub"""
    ls = [1, 3, 5]
    assert sub(ls, -3, 10) == [1, 3, 5]


def test_2use_sub() -> None:
    """Tests use case for sub"""
    ls = [1, 3, 5]
    assert sub(ls, 1, 3) == [3, 5]


def test_3use_sub() -> None:
    """Tests use case for sub"""
    ls = [1, 3, 5, 7, 9, 11]
    assert sub(ls, 2, 10) == [5, 7, 9, 11]


# add_at_index tests
def test_1use_add_at_index() -> None:
    """Tests expected output for add_at_index"""
    ls = [1, 3, 5, 7, 11]
    add_at_index(ls, 9, 4)
    assert ls == [1, 3, 5, 7, 9, 11]


def test_2edge_add_at_index():
    """Test that add_at_index raises an IndexError for an invalid index."""
    ls = []
    with pytest.raises(IndexError):
        add_at_index(ls, 99, 500)


def test_2use_add_at_index():
    """Tests expected output for add_at_index"""
    ls = [2, 4, 8]
    add_at_index(ls, 6, 2)
    assert ls == [2, 4, 6, 8]
