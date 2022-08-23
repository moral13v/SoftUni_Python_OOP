class Song:
    def __init__(self, name, length, single):
        self.single = single
        self.length = length
        self.name = name

    def get_info(self):
        return f"{self.name} - {self.length}"
