"""EX 03 Wordle"""

__author__ = "730768189"


def input_guess(secret_word_len: int) -> str:
    """Ensures guess is same length as secret word"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(word: str, letter: str) -> bool:
    """Searches through the word for instances of letter"""
    assert len(letter) == 1
    index: int = 0
    while index < len(word):
        if word[index] == letter:
            return True
        index += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Evaluates guesses to emojis (green for correct, yellow for wrong spot, etc.)"""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    toReturn: str = ""
    while index < len(secret_word):
        if secret_word[index] == guess[index]:
            toReturn += GREEN_BOX
        elif contains_char(secret_word, guess[index]):
            # Contains_char checks to see if letter exists in secret_word
            toReturn += YELLOW_BOX
        else:
            toReturn += WHITE_BOX
        index += 1
    return toReturn


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 0
    won: bool = False

    while turns < 6 and not won:
        print(f"=== Turn {turns+1}/6 ===")
        userGuess = input_guess(len(secret))
        if userGuess != secret:  # Checks guess is not the secret word
            print(emojified(userGuess, secret))
        else:
            print(emojified(userGuess, secret))
            # Still prints emoji version of correct guess
            won = True
        turns += 1

    if turns == 6 and not won:
        # User does not guess the word
        print("X/6 - Sorry, try again tomorrow!")
    else:
        print(f"You won in {turns}/6 turns!")


if __name__ == "__main__":
    main(secret="codes")
