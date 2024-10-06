"""EX04 - List Utils"""

__author__ = "730775156"


def all(list: list[int], num: int) -> bool:
    index: int = 0
    if len(list) == 0:
        return False
    while index < len(list):
        if list[index] != num:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 1
    biggest: int = input[0]
    if len(input) == 1:
        return biggest
    while index < len(input):
        if input[index] > biggest:
            biggest = input[index]
        index += 1
    return biggest


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    index: int = 0
    if len(list_1) != len(list_2):
        return False
    while index < len(list_1):
        if list_1[index] != list_2[index]:
            return False
        index += 1
    return True


def extend(list_a: list[int], list_b: list[int]) -> None:
    index: int = 0
    while index < len(list_b):
        list_a.append(list_b[index])
        index += 1
