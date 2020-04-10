# -*- codign: utf-8 -*-

import  random
# # Qué es una búsqueda binaria

# Los algoritmos son una serie de instrucciones que nos llevan a un resultado, por ejemplo que tal si queremos saber si un número se encuentra en una lista.

# Una forma es buscar un ítem tras otro, pero sí la lista es muy larga esta forma no es la mas eficiente, una forma mas eficiente de solucionar éste problema es usar una búsqueda binaria.

# Con el algoritmo de búsqueda binaria partimos de la lista ordenada, nosotros sabemos que hay números mayores y menores que el numero que estamos buscando.

# Seleccionamos un numero aleatorio para dividir la lista, puedes escoger cualquier número, en éste caso sumamos el primer y el último indice de la lista, los sumamos y dividimos en dos (por eso se llama binario), luego comparamos el número que esta en el indice, de esta manera ya eliminamos la mitad de las opciones. Podemos continuar dividiendo la lista y comparando hasta que lleguemos al resultado esperado.

def run():
    array = list()
    for element in range(random.randint(0, 100)):
        array.append(random.randint(element, 100))
    array.sort() # Order Array

    number = int(input("Number to Find:"))
    endIndex = len(array) - 1
    response = binarySearch(array, number, 0, endIndex)
    message = 'Su resultado fue: '
    if response > -1:
        message += "EXISTOSO, en la posición {}, siendo el valor {} de toda la lista: \n{}".format(response, number, array)
    else:
        message += "Erroneo, no existe el número en la lista"
    print(message)

def binarySearch(array, number, initIndex, endIndex):
    if initIndex > endIndex: # Over index
        return -1
    position = int((initIndex + endIndex) / 2) # Get middle index
    if array[position] == number: # Find the number
        return position
    elif array[position] > number:
        return binarySearch(array, number, initIndex, position - 1)
    else:
        return binarySearch(array, number, position + 1, endIndex)



if __name__ == "__main__":
    run()