"""EX06 Dictionaries"""

__author__ = "730768189"


def invert(dc: dict[str, str]) -> dict[str, str]:
    """Switches dictioanry keys with values"""
    dcKeys = list(dc.keys())
    dcValues = list(dc.values())
    newDict = {}
    for i in range(len(dcKeys)):
        if dcValues[i] in newDict:
            raise KeyError("That key already exists!")
        else:
            newDict[dcValues[i]] = dcKeys[i]
    return newDict


def favorite_color(dc: dict[str, str]) -> str:
    """Returns most repeated color in dictionary"""
    count = {}
    for item in list(dc.values()):
        if item in count:
            count[item] += 1
        else:
            count[item] = 0
    values = list(count.values())
    largestNum = -1
    largestColor = ""
    for i in range(len(values)):
        if values[i] > largestNum:
            largestNum = values[i]
            largestColor = list(count.keys())[i]
    return largestColor


def count(ls: list[str]) -> dict[str, int]:
    """Counts occurance of items in list"""
    toReturn = {}
    for item in ls:
        if item in toReturn:
            toReturn[item] += 1
        else:
            toReturn[item] = 0
    return toReturn


def alphabetizer(ls: list[str]) -> dict[str, list[str]]:
    """Returns dictionary with key being letter and values
    being all words starting with the key"""
    toReturn = {}
    for item in ls:
        item = item.lower()
        firstLetter = item[0]
        if firstLetter in toReturn:
            toReturn[firstLetter].append(item)
        else:
            toReturn[firstLetter] = [item]
    return toReturn


def update_attendance(dc: dict[str, list[str]], day: str, student: str) -> None:
    """Creates list of students present and stores in dictionary by day"""
    if day in dc:
        dc[day].append(student)
    else:
        dc[day] = [student]
