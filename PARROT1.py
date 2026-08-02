class Parrot():
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

blue = Parrot("Blue", 12)
woo = Parrot("Woo",15)

blue.display()
woo.display()

print(f"Blue's species is {blue.species}")
print(f"Woo's species is also {woo.species}")
