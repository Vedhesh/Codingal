class Parrot():
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def sing(self, song):
        print(f"{self.name} is now singing {song}!")

    def dancing(self):
        print(f"{self.name} is now dancing!")

blue = Parrot("Blue", 12)

blue.sing("Happy Birthday")
blue.dancing()



