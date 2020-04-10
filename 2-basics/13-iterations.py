# Fors (Iteracones)

print(range(5)) # Secuencia 0, 1, 2, 3, 4

print(range(5, 40, 4)) # Secuencia de pasos desde el 5 hasta el 40 de 4 en 4

# For
for i in range(5):
    print(i)


for i in range(5):
    print('Hello World')

# Example
for i in range(30):
  if i % 3 != 0:
    continue
  else:
    print(i**2)


for i in range(30):
    if i % 3 == 0: # i is divisible entre 3
        print("{} ** 2 = {}".format(i,i**2))
    elif i == 22:
        break

# Strings
stringTemp = "Miguel"
for letter in stringTemp:
    print(letter)