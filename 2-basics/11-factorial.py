# -*- coding: utf-8 -*-

# Recursión o Recursividad

# 1!, 2! , 3!, 4!
# 1! = 1
# 2! = 2 x 1 = 2
# 3! = 3 X 2 X 1 = 6
# 4! = 4 X 3 X 2 X 1 = 24
# 5! = 5 X 4 X 3 X 2 X 1 = 120
def run():
    number = int(input("Write a number: "))
    result = fat(number)
    print(result)

    result = factorial(number)
    print(result)

calc = 0
def fat(number):
    if number == 0: return 1 # Property Factorials

    size = (number + 1)
    result = ""
    for i in range(1, number + 1):
        size -= 1
        result += str(size)
        if(i < number):
            # result += " X "
            result += " X "
    return str(number) + "!: " + result

def factorial(number):
    if number == 0: return 1 # Property Factorials
    return number * factorial(number - 1)

# Start Software
if __name__ == "__main__":
    run()