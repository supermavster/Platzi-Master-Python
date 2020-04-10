# Tipos de datos en Python

## Enteros (int):

En este grupo están todos los números, enteros y long:

**Ejemplo:**

> 1, 2, 3, 2121, 2192, -123

---

## Booleanos (bool):

Son los valores falso o verdadero, compatibles con todas las operaciones booleanas ( and, not, or ):

**Ejemplo:**

> True, False

---

## Cadenas (str):

Son una cadena de texto:

**Ejemplo:**

> “Hola”, “¿Cómo estas?”

---

## Listas:

Son un grupo o array de datos, puede contener cualquiera de los datos anteriores:

**Ejemplo:**

> [1,2,3, ”hola” , [1,2,3] ], [1,“Hola”,True ]

Las listas las declaras con corchetes. Estas pueden tener una lista dentro o cualquier tipo de dato.

```
 >>> L = [22, True, ”una lista”, [1, 2]]
 >>> L[0]
 22
```

---

## Diccionarios:

Son un grupo de datos que se acceden a partir de una clave, parecidos a los objetos o JSONs:

**Ejemplo:**

> {“clave”:”valor”}, {“nombre”:”Fernando”}

En los diccionarios tienes un grupo de datos con un formato: la primera cadena o número será la clave para acceder al segundo dato, el segundo dato será el dato al cual accederás con la llave. Recuerda que los diccionarios son listas de llave:valor.

```
 >>> D = {"Kill Bill": "Tamarino", "Amelie": "Jean-Pierre Jeunet"}
 >>> D["Kill Bill"]
 "Tamarino"
```

---

## Tuplas:

También son un grupo de datos igual que una lista con la diferencia que una tupla después de creada no se puede modificar.

**Ejemplo:**

> (1,2,3, ”hola” , (1,2,3) ), (1,“Hola”,True)

Las tuplas se declaran con paréntesis, recuerda que **no puedes** editar los datos de una tupla después de que la has creado.

```
 >>> T = (22, True, "una tupla", (1, 2))
 >>> T[0]
 22
```

Nota: _(Pero jamás podremos cambiar los elementos dentro de esa Tupla)_

**_En Python trabajas con módulos y ficheros que usas para importar las librerías._**

---
