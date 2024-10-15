"""Summing the elements of a list using different loops"""

__author__ = "730775156"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    answer: float = 0.0
    if len(vals) == 0:
        answer = 0.0
    while index < len(vals):
        answer += vals[index]
        index += 1
    return answer


def f_sum(vals: list[float]) -> float:
    answer: float = 0.0
    for elem in vals:
        answer += elem
    return answer


def f_range_sum(vals: list[float]) -> float:
    answer: float = 0.0
    for index in range(0, len(vals)):
        answer += vals[index]
    return answer
