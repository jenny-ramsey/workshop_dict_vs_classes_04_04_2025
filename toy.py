# 1. Create the class so that it is a blue print. Always with def__init__ and self
# 2. List the toy options
# 3. Create the functions for print names and print colours
# 4. Classes use functions and lists instead of dictionaries 

class Toy:
    def __init__ (self, name, colour):
        self.name = name
        self.colour = colour

toys = [
    Toy("Ball", "red"),
    Toy("Teddy", "brown")
    ]

def print_names():
    for toy in toys:
        print(toy.name)

def print_colours():
        return [toy.colour for toy in toys]

print_names()
print(print_colours())

