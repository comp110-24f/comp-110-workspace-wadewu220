__author__ = "730775156"
from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_use_case() -> None:
    input: list[int] = [5, 2, 3, 5, 1]
    assert find_and_remove_max(input) == 5


def test_find_and_remove_max_use_case_2() -> None:
    input: list[int] = [1, 8, 2, 3, 3]
    find_and_remove_max(input)
    assert input == [1, 2, 3, 3]


def test_find_and_remove_max_edge_case() -> None:
    input: list[int] = []
    assert find_and_remove_max(input) == -1
