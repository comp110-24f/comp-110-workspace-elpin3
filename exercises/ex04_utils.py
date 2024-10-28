"""EX 04 CHARDLE (weird list concatination)"""

__author__ = "730768189"


def all(l1: list[int], num: int) -> bool:
    """Determines if a list (l1) is made up of only num passed (num)"""
    if len(l1) == 0:
        return False

    index = 0
    while index < len(l1):
        if l1[index] != num:
            return False
        index += 1
    return True


def max(l1: list[int]) -> int:
    """Returns largest number in list passed"""
    if len(l1) == 0:
        raise ValueError("max() arg is an empty List")
    # Prevents empty string being passed

    largestNum = l1[0]
    index = 0
    while index < len(l1):
        if l1[index] > largestNum:
            largestNum = l1[index]
        index += 1
    return largestNum


def is_equal(l1: list[int], l2: list[int]) -> bool:
    """Checks to see if two lists are the exact same"""
    if len(l1) != len(l2):  # If this argument is true then the lists are not equal
        return False
    index = 0
    while index < len(l1):
        if l1[index] != l2[index]:
            return False
        index += 1
    return True


def extend(l1: list[int], l2: list[int]) -> None:
    """Adds l2 values to end of l1"""
    index = 0
    while index < len(l2):
        l1.append(l2[index])
        index += 1
