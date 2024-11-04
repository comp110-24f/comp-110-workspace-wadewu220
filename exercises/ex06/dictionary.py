"""EX06 Utility Functions"""

__author__ = "730775156"


def invert(input: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}
    for key in input:
        if input[key] in inverted:
            raise KeyError("Error: duplicate key")
        inverted[input[key]] = key
    return inverted


def favorite_color(input: dict[str, str]) -> str:
    colors: list[str] = []
    color_count: dict[str, int] = {}
    if len(input) == 0:
        return ""
    for key in input:
        if input[key] in color_count:
            color_count[input[key]] += 1
        else:
            color_count[input[key]] = 1
            colors.append(input[key])
    popular: str = colors[0]
    for elem in color_count:
        if color_count[elem] > color_count[popular]:
            popular = elem
    return popular


def count(input: list[str]) -> dict[str, int]:
    new_dict: dict[str, int] = {}
    for elem in input:
        if elem in new_dict:
            new_dict[elem] += 1
        else:
            new_dict[elem] = 1
    return new_dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    new_dict: dict[str, list[str]] = {}
    for elem in input:
        letter: str = elem.lower()[0]
        if letter in new_dict:
            new_dict[letter].append(elem)
        else:
            new_dict[letter] = [elem]
    return new_dict


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    if day in input:
        if student not in input[day]:
            input[day].append(student)
    else:
        input[day] = [student]
    return None
