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


def flavor(taste: str, percent: float) -> None:
    print("This flavor is " + str(percent) + "% " + taste)


flavor(taste="umami", percent=100)


def greet(name: str) -> str:
    print("Hello " + name)
    print("The first letter of your name is " + str(name[0]))
    print("The last letter of your name is " + str(name[-1]))
    return "It's so nice to see you, " + name + "!"


def main() -> None:
    print(greet(name="Semi"))


main()


def have_done(task: str, completed: bool) -> str:
    return "Completed" + task + ":" + str(completed)


print(have_done(task="homework", completed=False))


def make_jersey(name: str, number: int) -> str:
    print(name + " is number" + str(jersey_num(number=number)))
    return name + ":" + str(number + 1)


def jersey_num(number: int) -> int:
    return number + 1


print(make_jersey(name="Wu", number=10))
print(int(4.8))


def name_eval(name: str) -> bool:
    return len(name) % 2 == 0


print(name_eval(name="Semi"))


def speak(sound: str, repeat: int) -> None:
    print(sound * repeat)


print(speak(sound="woof", repeat=3))
