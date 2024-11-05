"""File to define Fish class."""

__author__ = "730775156"


class Fish:
    """Creating Fish class."""

    age: int

    def __init__(self):
        """Initializes age to 0."""
        self.age = 0
        return None

    def one_day(self):
        """Age increases by 1 each day."""
        self.age += 1
        return None
