from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        total_comfort = sum([deco.comfort for deco in self.decorations])
        return total_comfort

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        output = f"{self.name}:\n"
        if not self.fish:
            output += f"Fish: none\n"
        else:
            output += f"Fish: {' '.join([fish.name for fish in self.fish])}\n"
        output += f"Decorations: {len(self.decorations)}\n"
        output += f"Comfort: {self.calculate_comfort()}"

        return output



