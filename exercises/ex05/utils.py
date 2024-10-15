"""List Utility Functions"""

__author__ = "730775156"


def only_evens(input: list[int]) -> list[int]:
    even_list: list[int] = []
    index: int = 0
    while index < len(input):
        if input[index] % 2 == 0:
            even_list.append(input[index])
        index += 1
    return even_list


def sub(input: list[int], num_1: int, num_2: int) -> list[int]:
    new_list: list[int] = []
    if num_1 < 0:
        num_1 = 0
    if num_2 > len(input):
        num_2 = len(input)
    if len(input) == 0 or num_1 >= len(input) or num_2 <= 0:
        return new_list
    for index in range(num_1, num_2):
        new_list.append(input[index])
    return new_list


def add_at_index(input: list[int], number: int, index: int) -> None:
    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")
    if index == len(input):
        input.append(number)
    else:
        input.append(0)
        for idx in range(len(input) - 1, index, -1):
            input[idx] = input[idx - 1]
        input[index] = number
