class Human:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def display(self):
        print(f"Name is {self.name} and height is {self.height}")


name = input("Enter name: ")
height = int(input("Enter height in inches: "))

human = Human(name, height)
human.display()

