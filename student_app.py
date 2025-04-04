# use an import to carry over classes from other files. The file in this case is called toy and we are 
# importing the class Toy

from toy import Toy

toys = [
    {
        "name": "Ball",
        "colour": "red"
    },
    {
        "name": "Teddy",
        "colour": "brown"
    }
]

# Make a toys list with at least 2 dictionaries representing a toy with name and colour DONE

# Task- create a function to print out the name of all toys

# notes on the process:
# 1. create the function first 
# 2. create a for loop to iterate through the toys
# 3. print just the name of the toys- use square brackets to iterate through
# 4. call the function again

def print_names():
    for toy in toys:
        print(toy["name"])
print_names()

# Task - create a function to print out all colours of toys. print(print_colours()) => ['red', 'green']
# notes - this prints the function out in the print instead of calling it

def print_colours():
    return [toy ["colour"] for toy in toys]
print(print_colours())


# take it further by storing it in a variable

colours = print_colours()
print(colours)

        
# Now do this with classes- see toy.py


