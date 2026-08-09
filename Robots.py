class Robot:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"My name is {self.name}!")

tom = Robot("Tom")
jerry = Robot("Jerry")

tom.introduce()
jerry.introduce()