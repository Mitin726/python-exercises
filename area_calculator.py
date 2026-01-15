import math

welcome = "==============================\nWelcome to the Area Calculator!\nPlease enter the figure you want to calculate its area...\n=============================="
options = """
============
1. Square.
2. Rectangle.
3. Triangle.
4. Circle.
5. Quit.
============
"""

print(welcome)
figure = int(input(options))
while figure != 5:
    if figure == 1:
        side = float(input("Write the Square's side: "))
        area = side ** 2
        print(f"The Square's area is {area}")
    elif figure == 2:
        length = float(input("Write the Rectangle's length: "))
        width = float(input("Now, write it's width: "))
        area = length * width
        print(f"The Rectangle's area is {area}")
    elif figure == 3:
        height = float(input("Write the Triangle's height: "))
        base = float(input("Now, write it's base: "))
        area = (height*base)/2
        print(f"The Triangle's area is {area}")
    elif figure == 4:
        radius = float(input("Write the Circle's radius: "))
        area = math.pi * (radius)**2
        print(f"The Circle's area is {area}")
    else: 
        print(f"\n{figure} is not a correct option...try again")
    figure = int(input(options))
print("Thank you for using the area calculator by Mitin726 :)")