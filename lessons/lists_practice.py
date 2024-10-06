my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

my_numbers.append(1.5)  # add an item to list

# print(my_numbers)

game_points: list[int] = [102, 86, 94]
game_points[1] = 72
game_points.pop(1)
# print(game_points)


def display(game_points: list[int]) -> None:
    index: int = 0
    while index < len(game_points):
        print(game_points[index])
        index += 1


# display(game_points)


def contains(needle: int, haystack: list[int]) -> bool:
    index: int = 0
    condition: bool = False
    while index < len(haystack) and not condition:
        if haystack[index] == needle:
            condition = True
        index += 1
    return condition


# print(contains(4, [4, 5, 6]))
