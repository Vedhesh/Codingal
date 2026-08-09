class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist - {name}, Genre - {genre}, is ready!")
    def add_song(self, song):
        self.songs.append(song)
        print(f"The song {song}, has been added to {self.name} ({self.genre})")
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"The song {song}, has been removed from {self.name} ({self.genre})")
        else:
            print(f"The song {song}, is not found in {self.name} ({self.genre})")
    def display(self):
        print(f"{self.name} ({self.genre}):")
        if self.songs:
            for i, s in enumerate(self.songs, 1):
                print(f"{i}. {s}")
        else:
            print("No songs exist, add some!")
    def __del__(self):
        print(f"{self.name} ({self.genre}) has been deleted.")

playlist = Playlist("Road trip mix", "Pop")
while True:
    choice = int(input("Action Panel: \n1. Add Song \n2. Remove Song \n3. View Playlist \n4. Delete Playlist"))
    if choice == 1:
        name = input("Enter song name to add --> ")
        playlist.add_song(name)
    elif choice == 2:
        name = input("Enter song name to delete --> ")
        playlist.remove_song(name)
    elif choice == 3:
        playlist.display()
    elif choice == 4:
        del playlist
    else:
        print("Invalid. Enter either 1, 2, 3 or 4...")