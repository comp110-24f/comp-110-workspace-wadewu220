"""EX01: Tea Party Planner"""

__author__ = "730775156"


def main_planner(guests: int) -> None:
    """Entrypoint of this program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))  # prints number of tea bags needed
    print("Treats: " + str(treats(guests)))  # prints number of treats needed
    print(
        "Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests)))
    )  # prints total cost of party


# Took me some time to figure out how to use concatenation to get the desired lines
# I realized that I had to convert the outputs of the functions into strings


def tea_bags(people: int) -> int:
    """Number of teabags needed"""
    return 2 * people


def treats(people: int) -> int:
    """Number of treats needed"""
    return int(1.5 * tea_bags(people=people))


# Didn't use keyword argument at first; changed after gradescope feedback


def cost(tea_count: int, treat_count: int) -> float:
    """Total cost"""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party?"))
    )  # passes user input as an argument to guests
