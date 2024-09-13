def eat(food: str) -> None:
    print("eating " + food)


def sigma(food: str) -> None:
    eat(food=food)


sigma(food="apple")


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


main()


def check_first_letter(word: str, letter: str) -> None:
    if word[0] == letter:
        print("match!")
    else:
        print("no match!")


print(check_first_letter(word="semi", letter="s"))
print(check_first_letter(word="jalen", letter="f"))
