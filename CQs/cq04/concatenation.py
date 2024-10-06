"""CQ04 - Concatenation"""

__author__ = "730775156"


def concat(first_word: str, second_word: str) -> str:
    return first_word + second_word


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
