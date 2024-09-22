"""CQ00 Mimic"""

__author__ = "730768189"


# Returns submitted message to user
def mimic(message: str) -> str:
    """Returns submitted message to user"""
    return message


# Replies to user with greeting
def main() -> None:
    """Calls mimic to greet user with inputted data"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
