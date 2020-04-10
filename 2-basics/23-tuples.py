# -*- codign: utf-8 -*-
# ## Tuplas:

# También son un grupo de datos igual que una lista con la diferencia que una tupla después de creada no se puede modificar.

# **Ejemplo:**

# > (1,2,3, ”hola” , (1,2,3) ), (1,“Hola”,True)

# Las tuplas se declaran con paréntesis, recuerda que **no puedes** editar los datos de una tupla después de que la has creado.

# ```
#  >>> T = (22, True, "una tupla", (1, 2))
#  >>> T[0]
#  22
# ```

# Nota: _(Pero jamás podremos cambiar los elementos dentro de esa Tupla)_

# **_En Python trabajas con módulos y ficheros que usas para importar las librerías._**

# ---


myTuple = (1, 2, 3) # (1,)
print(type(myTuple))
print(myTuple[0])
# myTuple[1] = 15 # TypeError: 'tuple' object does not support item assignment


# Vamos a construir un programa que nos permita encontrar el primer carácter que no se repite en un string.
# Por ejemplo si tenemos el string mimamameama el primer carácter que no se repite es la i.

def run():
    message = str(input("Get a string:\n"))
    response = getFirstUniqueCharacter(message)
    print("El primer carácter que no se repite es: {}\nDe la frase {}".format(response, message))

def getFirstUniqueCharacter(message):
    elements = {}
    message = message.replace(" ","").split()
    for word in message:
        for letter in word:
            if letter not in elements:
                elements[letter] = 0
            else:
                elements[letter] = elements[letter] + 1

    flag = 0
    response = ''
    for key, value in elements.items():
        if value <= flag and (response == '' or value != elements[response]): # revisar!!!
            flag = value
            response = key
        # else:
        print("{}: {}".format(key, value))

    return response


if __name__ == "__main__":
    run()
