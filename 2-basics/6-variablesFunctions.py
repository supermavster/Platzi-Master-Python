# hello = 'hola pianola'

# print(hello) # return Hola pianola

# def hello():
#     print('hola pianola')

# print(hello) # return the function

# Scope; Variables locales o globales

# -*- coding: utf-8 -*-
def run():
    print(' C A L C U L A T O R - Foreign Exchange ')
    print('Convert $ COP to $ USD \n')

    # Init Software
    init()

def init():
    # Python2: float(raw_input(""))
    amount = float(input("Enter the many COP:"))
    response = foreignExchangeCalculator(amount)
    print('Dollares ${} converted of ${}'.format(response, amount))

def foreignExchangeCalculator(amount):
    usdToCopRate = 4.010
    return usdToCopRate * amount

if __name__ == "__main__":
    run()