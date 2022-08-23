class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.mp = mp
        self.hp = hp
        self.name = name
        self.skills = {}
        self.guild = Player.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        output = f"Name: {self.name}\n" \
                 f"Guild: {self.guild}\n" \
                 f"HP: {self.hp}\n" \
                 f"MP: {self.mp}\n" \

        for key, value in self.skills.items():
            output += f"==={key} - {value}\n"

        return output


