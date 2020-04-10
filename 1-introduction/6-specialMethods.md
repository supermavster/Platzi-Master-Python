# Métodos especiales

## cmp(self,otro)

Método llamado cuando utilizas los operadores de comparación para **comprobar si tu objeto es menor, mayor o igual al objeto pasado como parámetro**.

---

## len(self)

> Método llamado para comprobar la longitud del objeto.

Lo usas, por ejemplo, cuando llamas la función len(obj) sobre nuestro código. Como es de suponer el método te debe devolver la longitud del objeto.

---

## init(self,otro)

> Estructura del constructor en una clase de Python

Es un constructor de nuestra clase, es decir, es un “método especial” que llamas automáticamente cuando creas un objeto.

---

## Condicionales IF

Los condicionales tienen la siguiente estructura. Ten en cuenta que lo que contiene los paréntesis es la comparación que debe cumplir para que los elementos se cumplan.

```
 if ( a > b ):
 	elementos
 elif ( a == b ):
 	elementos
 else:
 	elementos
```

---

## Bucle FOR

El bucle de for lo puedes usar de la siguiente forma:

- recorres una cadena o lista a la cual va a tomar el elemento en cuestión con la siguiente estructura:

```
 for i in ____:
 	elementos
```

**Ejemplo:**

```
 for i in range(10):
 	print i
```

En este caso recorrerá una lista de diez elementos, es decir el \_print i \_de ejecutar diez veces. Ahora i va a tomar cada valor de la lista, entonces este for imprimirá los números del 0 al 9

Recordar que en un **range** vas hasta el número puesto -1, en cortas palabras:

> 10 - 1 = 9

Siendo en total 10 elementos:

> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

---

## Bucle WHILE

En este caso while tiene una condición que determina hasta cuándo se ejecutará. O sea que dejará de ejecutarse en el momento en que la condición deje de ser cierta. La estructura de un while es la siguiente:

```
 while (condición):
 	elementos
```

**Ejemplo:**

```
  x = 0
 while x < 10:
  	print x
  	x += 1
```

**Explicación:**

1. Preguntará si es menor que diez.
2. Dado que es menor imprimirá x y luego sumará una unidad a x.
3. Luego x es 1 y como sigue siendo menor a diez se seguirá ejecutando.
4. Así sucesivamente hasta que x llegue a ser mayor o igual a 10.
