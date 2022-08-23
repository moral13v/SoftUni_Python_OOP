from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.core.validator import Validator
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

        self.successful_missions_count = 0
        self.not_completed_missions_count = 0


    def add_astronaut(self, astronaut_type: str, name: str):
        Validator.raise_if_invalid_astronaut_type(astronaut_type)

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type == Biologist.__name__:
            astronaut = Biologist(name)
        elif astronaut_type == Geodesist.__name__:
            astronaut = Geodesist(name)
        elif astronaut_type == Meteorologist.__name__:
            astronaut = Meteorologist(name)

        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(", ")

        self.planet_repository.add(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        if not self.astronaut_repository.find_by_name(name):
            raise Exception(f"Astronaut {name} doesn't exist!")
        astronaut = self.astronaut_repository.find_by_name(name)
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")

        planet = self.planet_repository.find_by_name(planet_name)

        suitable_astronauts = []

        for astronaut in sorted(self.astronaut_repository.astronauts, key=lambda a: a.oxygen, reverse=True):
            if astronaut.oxygen > 30:
                suitable_astronauts.append(astronaut)
            if len(suitable_astronauts) == 5:
                break

        if len(suitable_astronauts) <= 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        explorers_count = 0

        for astronaut in suitable_astronauts:
            explorers_count += 1
            for item in reversed(planet.items):
                if astronaut.oxygen > 0:
                    astronaut.breathe()
                    if astronaut.oxygen < 0:
                        break
                    astronaut.backpack.append(item)
                    planet.items.pop()
            if not planet.items:
                break

        if not planet.items:
            self.successful_missions_count += 1
            return f"Planet: {planet_name} was explored. {explorers_count} astronauts participated in collecting items."
        self.not_completed_missions_count += 1
        return "Mission is not completed."

    def report(self):
        result = f"{self.successful_missions_count} successful missions!\n" \
                 f"{self.not_completed_missions_count} missions were not completed!\n" \
                 f"Astronauts' info:\n"

        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}\n" \
                      f"Oxygen: {astronaut.oxygen}\n"
            if not astronaut.backpack:
                result += f'Backpack items: none\n'
            else:
                result += f"Backpack items: {', '.join(astronaut.backpack)}\n"

        return result


