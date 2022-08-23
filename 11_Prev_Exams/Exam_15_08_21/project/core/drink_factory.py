from project.drink.tea import Tea
from project.drink.water import Water


class DrinkFactory:
    def create_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if drink_type == "Tea":
            return Tea(name, portion, brand)
        if drink_type == "Water":
            return Water(name, portion, brand)
