# -*- codign: utf-8 -*-
# Un decoradores una función que recibe otra función y regresa una tercera función.
# Para reconocer un decorador, puedes ver que tienes un arroba sobre la declaración de una función.

def run():
    password = str(input("Write your password:\n"))
    protectedFunction(password)

def protected(func):
    def wrapper(password):
        if password == 'Supermavster':
            return func()
        else:
            print("The password is wrong")
    return wrapper

@protected
def protectedFunction():
    print("Your password is correct")

if __name__ == "__main__":
    run()