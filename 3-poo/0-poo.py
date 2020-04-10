# # Programación orientada a objetos en Python
# Los objetos nos permiten modelar objetos de la vida real, estos objetos van a tener un estado y métodos.
# De esta forma vamos a poder definir cada parte de nuestro código modelandolas cómo objetos.
# Encapsulación es una de las herramientas más poderosas que tienen los programadores, esta nos permite esconder la complejidad del software.

class Lamp:
    # Global Variables or Constants
    _LAMP = [
         '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''',
        '''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    '''
    ]

    def __init__(self, isTurnOn):
        self._isTurnOn = isTurnOn
    
    def turnOn(self):
        self._isTurnOn = True
        self._displayImages()


    def turnOff(self):
        self._isTurnOn = False
        self._displayImages()

    def _displayImages(self):
        if self._isTurnOn:
            print(self._LAMP[1] + '\n')
        else:
            print(self._LAMP[0]+ '\n')

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