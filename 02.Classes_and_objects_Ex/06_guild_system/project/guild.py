from project.player import Player


class Guild:
    def __init__(self, name: str, ):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = Player.DEFAULT_GUILD
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        output = f"Guild: {self.name}\n"
        for player in self.players:
            output += player.player_info()
        return output


