from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for curr_album in self.albums:
            if curr_album.name == album.name:
                return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for curr_album in self.albums:
            if curr_album.name == album_name:
                if curr_album.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(curr_album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        output = f"Band {self.name}"
        for album in self.albums:
            output += f"\n{album.details()}"
        return output

