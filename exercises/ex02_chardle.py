"""EX 02 CHARDLE (Worlde knock-off)"""

__author__ = "730768189"


def input_word() -> str:
    """Allows user to give a word and determines wether or not its valid"""
    word = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        quit()  # Appropriate placement for quit() bc no need to print anything else
    return word


def input_letter() -> str:
    """Allows user to give a letter and determines wether or not its valid"""
    char = input("Enter a single character: ")
    if len(char) != 1:
        print("Error: Character must be a single character.")
        quit()  # Appropriate placement for quit() bc no need to print anything else
    return char


def contains_char(input_word: str, input_letter: str) -> None:
    """Checks if the input_letter is inside of input_word"""
    print("Searching for " + input_letter + " in " + input_word)
    count: int = 0
    if input_word[0] == input_letter:
        print(input_letter + " found at index 0")
        count += 1
    if input_word[1] == input_letter:
        print(input_letter + " found at index 1")
        count += 1
    if input_word[2] == input_letter:
        print(input_letter + " found at index 2")
        count += 1
    if input_word[3] == input_letter:
        print(input_letter + " found at index 3")
        count += 1
    if input_word[4] == input_letter:
        print(input_letter + " found at index 4")
        count += 1
    # Lines 27-41 make my soul hurt. I am thankful for for loops
    if count == 0:
        print("No instances of " + input_letter + " in " + input_word)
    else:
        print(str(count) + " instances of " + input_letter + " found in " + input_word)


def main():
    contains_char(input_word=input_word(), input_letter=input_letter())
    """At first declared different variables to store values for input_word() and
    input_letter(). The method in the guide paper was much more efficient
    """


if __name__ == "__main__":
    main()
