"""CQ07 Find Max"""

__author__ = "730768189"


def find_and_remove_max(ls: list[int]) -> int:
    if len(ls) == 0:
        return -1
    max = ls[0]
    for item in ls:
        if item > max:
            max = item
    index = 0
    while index < len(ls):
        if max == ls[index]:
            ls.pop(index)
        else:
            index += 1
    return max
