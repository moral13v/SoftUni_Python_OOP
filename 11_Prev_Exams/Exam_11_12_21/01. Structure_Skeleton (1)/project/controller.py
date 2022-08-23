from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")
        if car_type == "MuscleCar":
            car = MuscleCar(model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."
        elif car_type == "SportsCar":
            car = SportsCar(model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        current_driver = None
        for driver in self.drivers:
            if driver.name == driver_name:
                current_driver = driver

        if current_driver not in self.drivers:
            raise Exception(f"Driver {driver_name} could not be found!")

        for car in reversed(self.cars):
            if car.__class__.__name__ == car_type and car.is_taken is False:
                if not current_driver.car:
                    current_driver.car = car
                    car.is_taken = True
                    return f"Driver {driver_name} chose the car {car.model}."
                else:
                    previous_car = current_driver.car
                    previous_car.is_taken = False
                    current_driver.car = car
                    car.is_taken = True
                    return f"Driver {driver_name} changed his car from {previous_car.model} to {car.model}."
        raise Exception(f"Car {car_type} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        current_race = None
        for race in self.races:
            if race.name == race_name:
                current_race = race

        if current_race not in self.races:
            raise Exception(f"Race {race_name} could not be found!")

        current_driver = None
        for driver in self.drivers:
            if driver.name == driver_name:
                current_driver = driver

        if current_driver not in self.drivers:
            raise Exception(f"Driver {driver_name} could not be found!")

        if current_driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if current_driver in current_race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        current_race.drivers.append(current_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        current_race = None
        for race in self.races:
            if race.name == race_name:
                current_race = race

        if current_race not in self.races:
            raise Exception(f"Race {race_name} could not be found!")

        if len(current_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_car_drivers = sorted(current_race.drivers, key=lambda driver: driver.car.speed_limit, reverse=True)

        output = ""

        for driver in fastest_car_drivers[0:3]:
            driver.number_of_wins += 1
            output += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"

        return output.strip()


















