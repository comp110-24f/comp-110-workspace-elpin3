"""Utils"""

__author__ = "730768189"


def only_evens(ls: list[int]) -> list[int]:
    newLs = []
    for item in ls:
        if item % 2 == 0:
            newLs.append(item)

    return newLs


def sub(ls: list[int], start: int, end: int) -> list[int]:
    if start < 0:
        start = 0
    if end > len(ls) - 1:
        end = len(ls)
    if len(ls) == 0 or start == end:
        return []
    lsToReturn = []
    for i in range(end - start):
        lsToReturn.append(ls[start + i])
    return lsToReturn


def add_at_index(ls: list[int], value: int, index: int) -> None:
    if index < 0 or index > len(ls):
        raise IndexError("Index is out of bounds for the input list")
    for i in range(index, len(ls) + 1):
        print(ls)
        if i == index:
            ls.append(value)
        if i > index:
            ls.append(ls[index])
            ls.pop(index)
