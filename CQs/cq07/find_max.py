__author__ = "730775156"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    index: int = 1
    big_number: int = input[0]
    while index < len(input):
        if input[index] > big_number:
            big_number = input[index]
        index += 1
    idx: int = 0
    while idx < len(input):
        if input[idx] == big_number:
            input.pop(idx)
        idx += 1
    return big_number


a: list[int] = [2, 3, 4, 2, 8, 10, 11, 3, 15, 4, 15]
print(find_and_remove_max(a))
print(a)
