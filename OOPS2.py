class student:
    grade = 10
    name = "Vedesh"

    def intro(self):
        print("Hi I am a student")

    def details(self):
        print("I am ", self.name)
        print(", I study in Grade ", self.grade)

me = student()
me.intro()
me.details()