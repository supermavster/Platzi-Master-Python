# -*- codign: utf-8 -*-

# Manejo de strings en Python
#Un string es una secuencia de caracteres, donde cada caracter tiene un indice que inicia en cero, por ejemplo
myString = 'Miguel'
print(myString)
print(myString[0]) # M
print(myString[1]) # i
print(myString[2]) # g
print(myString[3]) # u
print(myString[4]) # e
print(myString[5]) # l

# Para conocer la longitud de un string podemos usar la funcion len

print(len(myString)) # 6

#Los string tienen algunos métodos útiles cómo:

print(myString.upper()) # retorna el string en máyusculas
print(myString.lower()) # retorna el string en minúscula
print(myString.find('G')) # retorna el índice donde se encuentra
print(myString.format(2)) 						
print(myString.join("123"))
print(myString.split())
print(myString.replace(myString,"Angel")) 
print(myString.strip("G")) 
print(myString.lower()) 
print(myString.startswith("G")) 
print(myString.find("U")) 
print(myString.upper()) 
print(myString.endswith("A")) 
print(myString.rstrip("EL")) 
print(myString.splitlines())
print(myString.count("IG"))
print(myString.index("M"))
print(myString.isdigit())
print(myString.lstrip())
print(myString.zfill(10))
