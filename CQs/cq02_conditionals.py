"""CQ02 Pratice with Conditionals"""

__author__ = "730768189"


def guess_a_number() -> None:
    secret: int = 7
    userGuess = int(input("Guess a number: "))
    print("Your guess was", userGuess)
    if userGuess == secret:
        print("You got it!")
    elif userGuess > secret:
        print("Your guess was too high! The secret number is", secret)
    else:
        print("Your guess was too low! The secret number is", secret)


if __name__ == "__main__":
    guess_a_number()
