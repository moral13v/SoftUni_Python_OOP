from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


def get_item_by_name(collection, name):
    for item in collection:
        if item.name == name:
            return item


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
            return f"Successfully added {decoration_type}."
        elif decoration_type == "Plant":
            self.decorations_repository.add(Plant())
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.decorations.append(decoration)
                self.decorations_repository.remove(decoration)
                return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = get_item_by_name(self.aquariums, aquarium_name)
        if fish_type == "FreshwaterFish":
            current_fish = FreshwaterFish(fish_name, fish_species, price)
            if aquarium.__class__.__name__ == "FreshwaterAquarium":
                return aquarium.add_fish(current_fish)
            else:
                return "Water not suitable."
        elif fish_type == "SaltwaterFish":
            current_fish = SaltwaterFish(fish_name, fish_species, price)
            if aquarium.__class__.__name__ == "SaltwaterAquarium":
                return aquarium.add_fish(current_fish)
            else:
                return "Water not suitable."
        else:
            return f"There isn't a fish of type {fish_type}."

    def feed_fish(self, aquarium_name):
        aquarium = get_item_by_name(self.aquariums, aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        aquarium = get_item_by_name(self.aquariums, aquarium_name)
        fish_value = sum([fish.price for fish in aquarium.fish])
        decorations_value = sum([deco.price for deco in aquarium.decorations])
        total_value = fish_value + decorations_value
        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        output = ''
        for aquarium in self.aquariums:
            output += str(aquarium) + '\n'
        return output.strip()






