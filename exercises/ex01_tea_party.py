"""Example Problem #1 COMP 110 Section 2 - Tea Party Planner"""

__author__ = "730768189"


def main_planner(guests: int) -> None:
    """Uses all functions to calculate needs for tea party"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))
    # Had to use concatination instead of commas due to dollar sign placement
    # Thought about storing tea_bags(guests) and treats(guests) in variables


def tea_bags(people: int) -> int:
    """Determine number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """Determine number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Determine the cost of the tea party"""
    return tea_count * 0.5 + treat_count * 0.75
    # Did not need to add parenthesis to ensure multiplication before addition


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
