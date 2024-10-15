"Testing List Utility Functions"
__author__ = "730775156"
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_edge_case() -> None:
    input: list[int] = []
    assert only_evens(input) == []


def test_only_evens_use_case() -> None:
    input: list[int] = [1, 2, 3, 4]
    assert only_evens(input) == [2, 4]


def test_only_evens_use_case_2() -> None:
    input: list[int] = [1, 2, 3, 4]
    only_evens(input)
    assert input == [1, 2, 3, 4]


def test_sub_edge_case() -> None:
    input: list[int] = [10, 20, 30, 40]
    assert sub(input, -1, 6) == [10, 20, 30, 40]


def test_sub_use_case() -> None:
    input: list[int] = [10, 20, 30, 40]
    assert sub(input, 1, 3) == [20, 30]


def test_sub_use_case_2() -> None:
    input: list[int] = [10, 20, 30, 40]
    sub(input, 1, 3)
    assert input == [10, 20, 30, 40]


def test_add_at_index_edge_case() -> None:
    input: list[int] = []
    add_at_index(input, 1, 0)
    assert input == [1]


def test_add_at_index_use_case() -> None:
    input: list[int] = [10, 20, 30, 40]
    assert add_at_index(input, 15, 1) == None


def test_add_at_index_use_case_2() -> None:
    input: list[int] = [10, 20, 30, 40]
    add_at_index(input, 15, 1)
    assert input == [10, 15, 20, 30, 40]
