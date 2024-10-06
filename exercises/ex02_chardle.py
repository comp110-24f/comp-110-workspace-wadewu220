"""EX02 - Chardle - A cute step towards Wordle."""

__author__ = "730775156"


def input_word() -> str:
    word_guess: str = input("Enter a 5-character word: ")
    if len(word_guess) != 5:  # rejects words with a length smaller or greater than 5
        print("Error: Word must contain 5 characters.")
        exit()
    return word_guess


# Had to think about where to insert exit() function
# First defined the condition as len() < 5 or len() > 5, but realized I could simplify


def input_letter() -> str:
    letter_guess: str = input("Enter a single character: ")
    if (
        len(letter_guess) != 1
    ):  # rejects guesses that contain more or less than 1 character
        print("Error: Character must be a single character.")
        exit()
    return letter_guess


def contains_char(word_entered: str, letter_wanted: str) -> None:
    print("Searching for " + letter_wanted + " in " + word_entered)
    if word_entered[0] == letter_wanted:
        print(letter_wanted + " found at index 0")
    if word_entered[1] == letter_wanted:
        print(letter_wanted + " found at index 1")
    if word_entered[2] == letter_wanted:
        print(letter_wanted + " found at index 2")
    if word_entered[3] == letter_wanted:
        print(letter_wanted + " found at index 3")
    if word_entered[4] == letter_wanted:
        print(letter_wanted + " found at index 4")
    count_letter: int = word_entered.count(letter_wanted)
    if count_letter == 0:
        print("No instances of " + letter_wanted + " found in " + word_entered)
    if count_letter == 1:
        print("1 instance of " + letter_wanted + " found in " + word_entered)
    if count_letter == 2:
        print("2 instances of " + letter_wanted + " found in " + word_entered)
    if count_letter == 3:
        print("3 instances of " + letter_wanted + " found in " + word_entered)
    if count_letter == 4:
        print("4 instances of " + letter_wanted + " found in " + word_entered)
    if count_letter == 5:
        print("5 instances of " + letter_wanted + " found in " + word_entered)


# I've never used the count() function before, so I had to familiarize myself with it"


def main() -> None:
    contains_char(word_entered=input_word(), letter_wanted=input_letter())


if __name__ == "__main__":
    main()
