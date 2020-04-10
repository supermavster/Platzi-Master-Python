# Secuencia existente en una nueva existencia


# Dictionary comprehension - list comprehension
# Dictionary comprehension y list comprehension nos permite 
# escribir listas o diccionarios de forma más sencilla.

## LISTAS
# Números pares
pares = []
for num in range(1,31):
    if num % 2 == 0:
        pares.append(num)
# Esto mismo lo podemos expresar con una list comprehension
print(pares)

# numero de la variable generada numero del rango (del 1 al 30) donde si esta variable generada numero es divisible (par)
pares = [num for num in range(1,31) if num % 2 == 0]
print(pares)

## Diccionarios

cuadrados = {}
for num in range(1, 11):
    cuadrados[num] = num ** 2
print(cuadrados)

cuadrados = {num: num ** 2 for num in range(1, 11)}
print(cuadrados)


# En informática, el azúcar sintáctico es un término acuñado por Peter J. Landin en 1964 para referirse a los añadidos a la sintaxis de un lenguaje de programación diseñados para hacer algunas construcciones más fáciles de leer o expresar. Esto hace el lenguaje “más dulce” para el uso por programadores: las cosas pueden ser expresadas de una manera más clara, más concisas, o de un modo alternativo que se prefiera, sin afectar a la funcionalidad del programa.