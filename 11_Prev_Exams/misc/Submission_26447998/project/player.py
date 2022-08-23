from project.core.validator import Validator


class Player:
    unique_names = set()

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_string_is_empty_raises(value, 'Name not valid!')
        # TO DO Check if player with same name exists
        Validator.check_if_player_with_same_name_exists_raises(
            value,
            Player.unique_names,
            f'Name {value} is already used!'
        )
        Player.unique_names.add(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError(f'The player cannot be under 12 years old!')
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError('Stamina not valid!')
        self.__stamina = value

    def __str__(self):
        return f'Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}'
