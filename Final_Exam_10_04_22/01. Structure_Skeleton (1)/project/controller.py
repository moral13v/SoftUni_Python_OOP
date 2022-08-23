class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        output = "Successfully added: "
        for player in players:
            if player not in self.players:
                self.players.append(player)
                output += f"{player.name}, "
        return output.rstrip(", ")

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in ["Food", "Drink"]:
            return

        player = None
        for p in self.players:
            if p.name == player_name:
                player = p

        supplies_by_type = [s for s in self.supplies if s.__class__.__name__]
        supply = None
        if supplies_by_type:
            supply = supplies_by_type.pop()

        if player is None:
            return

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        if sustenance_type == "Food" and not supplies_by_type:
            raise Exception("There are no food supplies left!")

        if sustenance_type == "Drink" and not supplies_by_type:
            raise Exception("There are no drink supplies left!")

        result = player.stamina + supply.energy
        if result > 100:
            player.stamina = 100
        else:
            player.stamina = result

        self.supplies.remove(supply)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = [p for p in self.players if p.name == first_player_name][0]
        second_player = [p for p in self.players if p.name == second_player_name][0]

        if first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."

        if second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if first_player.stamina < second_player.stamina:

            result1 = second_player.stamina - first_player.stamina/2
            if result1 < 0:
                second_player.stamina = 0
                winner_name = first_player_name
                return f"Winner: {winner_name}"
            else:
                second_player.stamina = result1

            result2 = first_player.stamina - second_player.stamina/2
            if result2 < 0:
                first_player.stamina = 0
                winner_name = second_player_name
                return f"Winner: {winner_name}"
            else:
                first_player.stamina = result2

        elif first_player.stamina > second_player.stamina:

            result2 = first_player.stamina - second_player.stamina / 2
            if result2 < 0:
                first_player.stamina = 0
                winner_name = second_player_name
                return f"Winner: {winner_name}"
            else:
                first_player.stamina = result2

            result1 = second_player.stamina - first_player.stamina / 2
            if result1 < 0:
                second_player.stamina = 0
                winner_name = first_player_name
                return f"Winner: {winner_name}"
            else:
                second_player.stamina = result1

        winner_name = ''

        if first_player.stamina > second_player.stamina:
            winner_name = first_player_name
        elif second_player.stamina > first_player.stamina:
            winner_name = second_player_name

        return f"Winner: {winner_name}"

    def next_day(self):
        for player in self.players:

            result = player.stamina - player.age*2
            if result < 0:
                player.stamina = 0
            else:
                player.stamina = result

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        output = ''

        for player in self.players:
            output += str(player) + '\n'
        for supply in self.supplies:
            output += supply.details() + '\n'

        return output.strip()
