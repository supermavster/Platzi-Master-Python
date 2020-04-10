# -*- coding: utf-8 -*-
# ## Diccionarios:

# Son un grupo de datos que se acceden a partir de una clave, parecidos a los objetos o JSONs:

# **Ejemplo:**

# > {“clave”:”valor”}, {“nombre”:”Fernando”}

# En los diccionarios tienes un grupo de datos con un formato: la primera cadena o número será la clave para acceder al segundo dato, el segundo dato será el dato al cual accederás con la llave. Recuerda que los diccionarios son listas de llave:valor.

# ```
#  >>> D = {"Kill Bill": "Tamarino", "Amelie": "Jean-Pierre Jeunet"}
#  >>> D["Kill Bill"]
#  "Tamarino"
# ```

myDictionary = {}
myDictionary['firstValue'] = "Hola pianola"
myDictionary['secondValue'] = "Qué se dice"
print(myDictionary['secondValue'])

# example
myNotes = {}
myNotes['firstSemester'] = 4.1
myNotes['secondSemester'] = 3.1
myNotes['thirdSemester'] = 3.8
myNotes['fourthSemester'] = 4.0

# Iteration #1 (Keys):
for key in myNotes:
    print(key)

# Iteration #2 (Values):
for value in myNotes.values():
    print(value)

for key, value in myNotes.items(): # python2 => myNotes.iteritems()
    print("Key: {}, value: {}".format(key, value))

sumNotes = 0
for value in myNotes.values():
    sumNotes += value
print("Su nota final es: {}".format(sumNotes / len(myNotes)))