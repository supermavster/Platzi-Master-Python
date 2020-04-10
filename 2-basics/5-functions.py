# -*- coding: utf-8 -*-

# Scope: el ambito de aplicación de las variables

# # Example Plus
# def plus(numOne, numTwo):
#     return numOne + numTwo

# print(plus(2, 3)) # result: 5

# Turtle Example

# include library
import turtle

# Functions
def main():
    window = turtle.Screen() # Open a windows
    turtleObject = turtle.Turtle() # Generate a Turtle
    makeSqueare(turtleObject) # Make Squart
    turtle.mainloop() # Keep the windows

def makeSqueare(turtleObject):
    # Python2: raw_input()
    # Python3: 
    length = int(input("Size of the Squart: "))
    lines = int(input("Many sides: "))
    angle = int(input("Angle: "))

    for i in range(lines):
        # makeLineAndTurn(turtle, length, angle)
        makeLineAndTurn(turtleObject, length, angle)

def makeLineAndTurn(turtleObject, length, angle):
    turtleObject.forward(length)
    turtleObject.left(angle)

# Inicializa el proyecto a partir de lo que este dentro (start, init)
if __name__ == "__main__":
    main()
