"""File to define River class."""

__author__ = "730775156"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Creating River class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes fish older than 3 and bears older than 5."""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        for elem in self.fish:
            if elem.age <= 3:
                surviving_fish.append(elem)  # picks out fish that are 3 or younger
        self.fish = surviving_fish
        for elem in self.bears:
            if elem.age <= 5:
                surviving_bears.append(elem)  # picks out bears that are 5 or younger
        self.bears = surviving_bears
        return None

    def bears_eating(self):
        """Changes fish population and hunger score based on number of fish eaten."""
        for elem in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                elem.eat(3)
        return None

    def check_hunger(self):
        """Removes starved bears."""
        alive_bears: list[Bear] = []
        for elem in self.bears:
            if elem.hunger_score >= 0:
                alive_bears.append(elem)
        self.bears = alive_bears
        return None

    def repopulate_fish(self):
        """Adds baby fish to population."""
        idx: int = 0
        num_fish: int = len(self.fish)
        while idx < (num_fish // 2) * 4:
            self.fish.append(
                Fish()
            )  # adds four fish to population for each pair of fish
            idx += 1
        return None

    def repopulate_bears(self):
        """Adds baby bears to population."""
        idx: int = 0
        num_bears: int = len(self.bears)
        while idx < num_bears // 2:
            self.bears.append(
                Bear()
            )  # adds one bear to population for each pair of bears
            idx += 1
        return None

    def view_river(self):
        """Prints day, fish population, bear population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulates one week of life in river."""
        idx: int = 0
        while idx < 7:
            self.one_river_day()  # calls one_river_day() seven times
            idx += 1
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes fish from fish population."""
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)  # removes first [amount] elements from fish population
            idx += 1
        return None
