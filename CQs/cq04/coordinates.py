"""CQ04 - Coordinates"""

__author__ = "7307735156"


def get_coords(xs: str, ys: str) -> None:
    index: int = 0
    while index < len(xs):
        idx: int = 0
        while idx < len(ys):
            print(f"({xs[index]},{ys[idx]})")
            idx += 1
        index += 1


get_coords("hi", "bye")
