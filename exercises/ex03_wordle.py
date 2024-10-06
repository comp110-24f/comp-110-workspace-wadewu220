"""Exercise 03: Wordle"""

__author__ = "730775156"


def input_guess(num_char: int) -> str:
    guess: str = input(f"Enter a {num_char} character word: ")
    while len(guess) != num_char:
        guess = input(f"That wasn't {num_char} chars! Try again: ")
    return guess


def contains_char(word: str, letter: str) -> bool:
    """Checks if word contains letter"""
    assert len(letter) == 1
    index: int = 0
    condition: bool = True
    while index < len(word):
        if word[index] == letter:
            condition = True  # returns True if word contains letter
            return condition
        else:
            condition = False  # returns False if word does not contain letter
        index += 1
    return condition


def emojified(guess_word: str, secret_word: str) -> str:
    """Visualizes accuracy of guess through emojis"""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    copy: str = ""
    index: int = 0
    while index < len(guess_word):
        if guess_word[index] == secret_word[index]:
            copy += GREEN_BOX  # Adds green box if letter is right and in right place
        elif contains_char(word=secret_word, letter=guess_word[index]):
            copy += YELLOW_BOX  # Adds yellow box if letter is right but in wrong place
        else:
            copy += WHITE_BOX  # Adds white box if letter is wrong
        index += 1
    return copy


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # keeping track of player's turns
    lose: bool = True  # represents whether or not player has won game
    while turn <= 6 and lose:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(
            len(secret)
        )  # assigns player's guess to the variable guess
        print(emojified(guess_word=guess, secret_word=secret))
        if guess == secret:
            lose = False  # if player wins, exit while loop
        turn += 1
    if turn <= 7 and not lose:
        print(f"You won in {turn-1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
