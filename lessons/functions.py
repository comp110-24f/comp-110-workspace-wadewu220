"""Practice with functions"""

from random import randint

print(randint(1, 10))


# Define a function
def quotient(num1: int, num2: int) -> float:
    """Dividing two numbers"""
    return num1 / num2


# Call the function
print(quotient(16, 4))


def product(num1: int, num2: str) -> str:
    """Multiplying a string by an integer"""
    return num1 * num2


print(product(2, "eagles"))


def tof(num1: int, num2: int) -> bool:
    """Comparing two integers"""
    return num1 > num2


print(tof(num1=4, num2=8))

print(quotient(num1=randint(1, 10), num2=randint(1, 10)))
