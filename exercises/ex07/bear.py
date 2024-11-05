"""File to define Bear class."""

__author__ = "730775156"


class Bear:
    """Creating Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes age and hunger score to 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Age increases by 1 and hunger score decreases by 1 each day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Adjusts hunger score based on fish eaten."""
        self.hunger_score += num_fish
