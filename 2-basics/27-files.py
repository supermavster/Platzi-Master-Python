# -*- codign: utf-8 -*-

# # Files

# Manejo de archivos en Python
# Con Python también podemos leer y escribir archivos del sistema.

# Existen varios modos en los que podemos manejar archivos

# ‘r’ = leer
# ’w’ = escribir
# ’a’ = añadir
# ’r+’ = leer y escribir

# Siempre recuerda cerrar el archivo.

# El keyword with nos permite manejar el contexto al trabajar con archivos
def run():
    with open('numbers.txt', 'w') as fileTemp:
        for i in range(0, 9):
            fileTemp.write(str(i))

    with open("9-ZenPython") as fileTemp:
        text = (fileTemp.readlines())
        word = "obvia"
        print("'{}' se encuentra {}".format(word, [txt for txt in text if txt.count('obvia')]))

if __name__ == "__main__":
    run()