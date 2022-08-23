from project.core.validator import Validator
from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        result = f'Successfully added: '
        for player in players:
            if player not in self.players:
                self.players.append(player)
                result += f'{player.name}, '
        # CHECK FOR ERRORS IN CASE NO PLAYERS ADDED
        return result.strip(', ')

    def add_supply(self, *supplies):
        for sup in supplies:
            self.supplies.append(sup)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in ('Food', 'Drink'):
            return

        player = self.__find_player_by_name(player_name)

        if player is None:
            return
        if player.stamina == 100:
            return f'{player.name} have enough stamina.'

        supply = self.__find_last_supply_added_in_list_by_type(
            sustenance_type,
            f'There are no {sustenance_type.lower()} supplies left!'
        )
        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy
        self.supplies.remove(supply)
        return f'{player_name} sustained successfully with {supply.name}.'

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.__find_player_by_name(first_player_name)
        player2 = self.__find_player_by_name(second_player_name)
        players_stamina_check = Validator.check_players_stamina_for_duel(player1, player2)
        if players_stamina_check:  # In case one players stamina is 0
            return players_stamina_check

        first_attacker, second_attacker = sorted([player1, player2], key=lambda x: x.stamina)
        # First attack
        if second_attacker.stamina - (first_attacker.stamina / 2) <= 0:
            second_attacker.stamina = 0
            return f'Winner: {first_attacker.name}'
        else:
            second_attacker.stamina -= (first_attacker.stamina / 2)

        # Second attack
        if first_attacker.stamina - (second_attacker.stamina / 2) <= 0:
            first_attacker.stamina = 0
            return f'Winner: {second_attacker.name}'
        else:
            first_attacker.stamina -= (second_attacker.stamina / 2)

        if first_attacker.stamina > second_attacker.stamina:
            return f'Winner: {first_attacker.name}'
        else:
            return f'Winner: {second_attacker.name}'

    def next_day(self):
        for player in self.players:
            reduced_by = player.age * 2
            if player.stamina - reduced_by < 0:
                player.stamina = 0
            else:
                player.stamina -= reduced_by

        for player in self.players:
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = ''
        for player in self.players:
            result += f'{str(player)}\n'
        for supply in self.supplies:
            result += f'{supply.details()}\n'
        return result.strip()

    def __find_player_by_name(self, player_name: str):
        for pl in self.players:
            if pl.name == player_name:
                return pl

    def __find_last_supply_added_in_list_by_type(self, sustenance_type, message):
        for supply in self.supplies[::-1]:
            if supply.__class__.__name__ == sustenance_type:
                return supply
        raise Exception(message)

# controller = Controller()
# player1 = Player('Dobrin', 25)
# player2 = Player('Petur', 25)
# player3 = Player('Misho', 25)
# print(controller.add_player(player1, player2, player3))
# print(controller.add_player(player1))

