from project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.songs = list(songs)
        self.name = name
        self.published = False

    def contains_song(self, song_name):
        for album_song in self.songs:
            if album_song.name == song_name:
                return True
        return False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if self.contains_song(song.name):
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        for curr_song in self.songs:
            if curr_song.name == song_name:
                self.songs.remove(curr_song)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        output = f"Album {self.name}\n"
        for song in self.songs:
            output += f"== {song.get_info()}\n"
        return output





