"""Challenge Question 02"""

__author__ = "730775156"


def guess_a_number() -> None:
    secret: int = 7
    x: str = input("Guess a number: ")
    print("Your guess was " + x)
    if int(x) == secret:
        print("You got it!")
    elif int(x) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
