# -*- coding: utf-8 -*-
def run():
    number = int(input("Write a number: "))
    result = sumData(number)
    print(result)
    # Visual Process
    result = sumDataView(number)
    print(result)

calc = 0
def sumDataView(number):
    if number == 1: return 1
    size = (number)
    result = ""
    for i in range(1, number + 1):
        result += str(size)
        if(i < number):
            result += " + "
        size -= 1
    return str(number) + ": " + result

def sumData(number):
    if number == 1: return 1
    return number + sumData(number - 1)

# Start Software
if __name__ == "__main__":
    run()