def eat(food: str) -> None:
    print("eating " + food)


def sigma(food: str) -> None:
    eat(food=food)


def greet(name: str) -> str:
    print(
        "Hello, "
        + name
        + ", your name starts with an "
        + name[0]
        + " and ends with an "
        + name[-1]
    )
    return "Do you want to get a sweet treat with me, " + name + "?"


def main() -> None:
    print(greet(name="Semi"))


def check_first_letter(word: str, letter: str) -> None:
    if word[0] == letter:
        print("match!")
    else:
        print("no match!")


def remove_chars(msg: str, char: str) -> str:
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy = copy + msg[index]
        index += 1
    return copy


my_numbers = list()
print(my_numbers)

game_points: list[int] = [102, 86, 94]
game_points.append(94)
print(game_points)


pets: list[str] = ["Louie", "Bo", "Bear"]
for dogs in pets:
    print(f"Good boy, {dogs}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
