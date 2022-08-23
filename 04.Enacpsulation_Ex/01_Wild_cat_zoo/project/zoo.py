from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animal_expenses = 0
        for animal in self.animals:
            animal_expenses += animal.money_for_care
        if animal_expenses > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= animal_expenses
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        output = f"You have {len(self.animals)} animals"

        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)

        output += f"\n----- {len(lions)} Lions:\n"
        output += '\n'.join([repr(lion) for lion in lions])

        output += f"\n----- {len(tigers)} Tigers:\n"
        output += '\n'.join([repr(tiger) for tiger in tigers])

        output += f"\n----- {len(cheetahs)} Cheetahs:\n"
        output += '\n'.join([repr(cheetah) for cheetah in cheetahs])

        return output

    def workers_status(self):
        output = f"You have {len(self.workers)} workers"

        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            elif worker.__class__.__name__ == "Vet":
                vets.append(worker)

        output += f"\n----- {len(keepers)} Keepers:\n"
        output += '\n'.join([repr(keeper) for keeper in keepers])

        output += f"\n----- {len(caretakers)} Caretakers:\n"
        output += '\n'.join([repr(caretaker) for caretaker in caretakers])

        output += f"\n----- {len(vets)} Vets:\n"
        output += '\n'.join([repr(vet) for vet in vets])

        return output

