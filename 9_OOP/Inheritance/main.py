class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves.")

class Dog(Animal):
    def bark(self):
        print("Woof!")

d = Dog("Buddy")
d.move()  # inherited
d.bark()  # own method
