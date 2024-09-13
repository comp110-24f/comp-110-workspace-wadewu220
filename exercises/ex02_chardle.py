"""EX02 - Chardle - A cute step towards Wordle."""

__author__ = "730775156"


def input_word() -> str:
    word_guess: str = input("Enter a 5-character word: ")
    if len(word_guess) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word_guess


# Had to think about where to insert exit() function
# First defined the condition as len() < 5 or len() > 5, but realized I could simplify


def input_letter() -> str:
    letter_guess: str = input("Enter a single character: ")
    if len(letter_guess) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter_guess


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
    if word[1] == letter:
        print(letter + " found at index 1")
    if word[2] == letter:
        print(letter + " found at index 2")
    if word[3] == letter:
        print(letter + " found at index 3")
    if word[4] == letter:
        print(letter + " found at index 4")
    count: int = word.count(letter)
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count == 1:
        print("1 instance of " + letter + " found in " + word)
    if count == 2:
        print("2 instances of " + letter + " found in " + word)
    if count == 3:
        print("3 instances of " + letter + " found in " + word)
    if count == 4:
        print("4 instances of " + letter + " found in " + word)
    if count == 5:
        print("5 instances of " + letter + " found in " + word)


# I've never used the count() function before, so I had to familiarize myself with it"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
