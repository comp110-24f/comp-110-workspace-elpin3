"""CQ03 While Loops"""

__author__ = "730768189"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0  # Counts the number of times search_char found
    index: int = 0  # Used to iterate through the phrase
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count


num_instances(phrase="Happy Tuesday!", search_char="z")
