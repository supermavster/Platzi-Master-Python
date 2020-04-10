# Clases

Clases es uno de los conceptos con más definiciones en la programación, pero en resumen sólo son la representación de un objeto.

> Para definir la clase usas class y el nombre, en caso de tener parámetros los pones entre paréntesis.

```
class ExampleClass(parms):
    def helloWorld():
        return 'Hello World!'


testClass = ExampleCass(XXX)
print testClass.helloWorld()

> Hello World!
```

Para crear un **constructor** haces una función dentro de la clase con el nombre init y de parámetros self (significa su clase misma), nombre_r y edad_r:

```
class Student(object):
    def __init__(self, name, years):
        self.name = name
        self.years = years

    def helloWorld(self):
        return "My name is %s, I am %i years old" % (self.name, self.years)
```

Llamar la clase:

```
student = Student("Arturo", 21)
print student.helloWorld()

> My name is Arturo, I am 21 years old
```

Lo que hicimos en las dos últimas líneas fue:

1. En la variable e llamamos la clase Estudiante y le pasamos la cadena “Arturo” y el entero 21. _Notese que el tipo de dato lo define solo_

2. Imprimimos la función helloWorld() dentro de la variable e (a la que anteriormente habíamos pasado la clase).

Y por eso se imprime la cadena "My name is Arturo, I am 21 years old"
