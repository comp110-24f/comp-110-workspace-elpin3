"""Mutating functions."""

__author__ = "730768189"


def manual_append(l1: list[int], toAdd: int) -> None:
    l1.append(toAdd)


def double(l1: list[int]) -> None:
    index = 0
    while index < len(l1):
        l1[index] = l1[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
