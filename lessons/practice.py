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
# print(my_numbers)

game_points: list[int] = [102, 86, 94]
game_points.append(94)
# print(game_points)


# pets: list[str] = ["Louie", "Bo", "Bear"]
# for dogs in pets:
# print(f"Good boy, {dogs}!")

# names: list[str] = ["Alyssa", "Janet", "Vrinda"]
# for idx in range(0, len(names)):
# print(f"{idx}: {names[idx]}")


input: list[str] = ["Henry", "Tommy", "Silas"]
new_list: list[str] = []
for elem in input:
    for letter in elem:
        if letter == "a":
            new_list.append(elem)


def vowel_count(input: str) -> dict[str, int]:
    a_count: int = 0
    e_count: int = 0
    i_count: int = 0
    o_count: int = 0
    u_count: int = 0
    for letter in input:
        if letter == "a":
            a_count += 1
        if letter == "e":
            e_count += 1
        if letter == "i":
            i_count += 1
        if letter == "o":
            o_count += 1
        if letter == "u":
            u_count += 1
    vowel_list: dict[str, int] = {
        "a": a_count,
        "e": e_count,
        "i": i_count,
        "o": o_count,
        "u": u_count,
    }
    return vowel_list


def count(word: str) -> dict[str, int]:
    result: dict[str, int] = {}
    num: int = 0
    for idx in range(0, len(word)):
        char: str = word[idx]
        for letter in word:
            if letter == char:
                num += 1
        result[char] = num
        num = 0
    return result


print(count("richard"))
