10 == 10 # TRUE

'a' == 'a' # True

'miguel' == 'Miguel' # False: la m es M y no m en ascii es otro numero

10 > 15 # false

'z' > 'a' # True: porque el valor numerico del caracter z es mayor a 65 que es a en asccii

10 != 10 # False: son iguales

15 != 10 # True

10 >= 11 # False

15 <= 15 # true

10 > 15 and 15 > 20 
#  F    ^    F

'a' == 'a' and 'b' == 'b' # True

True and True # True

'a' == 'a' or 'b' != 'b' # True

True or False # True

False or False # False


def sayHello(age):
    if(age > 17):
        return "Hello Mister"
    else:
        return "Hello Boy"

if __name__ == "__main__":
    print(sayHello(18), sayHello(15), sayHello(22))