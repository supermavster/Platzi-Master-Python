# -*- codign: utf-8 -*-
from lamp import Lamp # Call the Library 

def run():
    lamp = Lamp(isTurnOn=False)
    
    while True:
        command = int(input("What is your action?\t\n1. Turn On\t\n2. Turn off\t\n3. Exit\n"))
        if command == 1:
            lamp.turnOn()
        elif command == 2:
            lamp.turnOff()
        elif command == 3:
            break
        else:
            print("The command is not found")


if __name__ == "__main__":
    run()