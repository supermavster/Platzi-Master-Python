# -*- coding: utf-8 -*-

# Verification any number to Prime Number
# Divisibles entre 1 y el mismo, puesto que todos los numeros se componen de los numeros primos

def run():
    number = int(input("Write a number: "))
    result = checkPrimeNumber(number)
    # Big Version
    check = "" if result else "NOT"
    print("Big: Your number {} is {} a prime number". format(number, check))
    # Short Version
    result = shortCheck(number)
    check = "" if result else "NOT"
    print("Short: Your number {} is {} a prime number". format(number, check))

def checkPrimeNumber(number):
    if number < 2: # If the number is minor to Two is not Prime
        return False
    elif number == 2: # If the number is equals to Two is Prime
        return True
    elif number > 2 and number % 2 == 0: # If the number is max to Two and the Mood is equals to 0 is not Prime
        return False;
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
    return True

def shortCheck(number):
    if  number < 2:
        return False
    else:
        for i in range(2, number):
                if number % i == 0:
                    return False
        return True

if __name__ == "__main__":
    run()