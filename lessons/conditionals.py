def less_than_10(num: int) -> None:
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("small number")
    elif num == 10:
        print("10")
    else:
        print("big number")


less_than_10(num=12)


def wake_up(alarm: bool) -> str:
    if alarm:
        return "Wake up"
    else:
        return "Sleep"


print(wake_up(alarm=True))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match"


print(check_first_letter(word="semi", letter="s"))


def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
