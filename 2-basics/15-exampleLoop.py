# -*- coding: utf-8 -*-

# Library 
import random

def run():
    numberFound = False
    sizeGame = int(input("Write the size of the game (number): "))
    # randomNumber = random.randint(0, 20)
    randomNumber = random.randint(0, sizeGame)
    while not numberFound: # is the same: !NumberFound or !false = true
        number = int(input("Write a number: "))
        # numberFound = (number == randomNumber) 
        if number == randomNumber:
            print('Congratulations!! You found the number.')
            numberFound = True
        elif number >= randomNumber:
            print("The number is more small than your number")
        else:
            print("The number is more big than your number")

# Start Software
if __name__ == "__main__":
    run()