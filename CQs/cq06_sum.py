"""Summing the elements of a list using different loops"""

__author__ = "730768189"


def w_sum(vals: list[float]) -> float:
    index = 0
    sum = 0.0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum = 0.0
    for item in vals:
        sum += item
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum = 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum
