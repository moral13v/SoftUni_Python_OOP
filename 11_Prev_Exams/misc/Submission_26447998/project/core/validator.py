class Validator:

    @staticmethod
    def check_if_string_is_empty_raises(string, message):
        if string == '':
            raise ValueError(message)

    @staticmethod
    def check_if_player_with_same_name_exists_raises(name, players, message):
        if name in players:
            raise Exception(message)

    @staticmethod
    def check_players_stamina_for_duel(player1, player2):
        check_players_stam_res = ''
        if player1.stamina > 0 and player2.stamina > 0:
            return None
        for pl in [player1, player2]:
            if pl.stamina == 0:
                check_players_stam_res += f'Player {pl.name} does not have enough stamina.\n'
        return check_players_stam_res.strip()
