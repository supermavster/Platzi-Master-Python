# Operaciones con Lists en Python

#Unir Lists
myList = [1]
ListTwo = [2,3,4]
ListThree = myList + ListTwo
print(ListThree) # [1,2,3,4]

# Multiplicar elementos
myList = ['a']
ListTwo = myList * 5
print(ListTwo) # ['a','a','a','a','a']

# Dividir Lists
myList = [1,2,3,4,5]
myList_reversed = myList[::-1]
print(myList_reversed) # [5,4,3,2,1]

# Eliminar último elemento de la List
myList = [1,2,3,4,5]
myList = myList.pop()
print(myList) # [1,2,3,4]

# Ordenar la List
myList = [2,1,5,4,3]
myList = myList.sort()
print(myList) # [1,2,3,4,5]

# Eliminar un elemento
myList = [1,2,3,4,5]
del myList[0]
print(myList) # [2,3,4,5]

# extend 
myList = [1,2,3,4,5]
ListTwo = [6,7,8]
myList.extend(ListTwo)
print(myList) # [1, 2, 3, 4, 5, 6, 7, 8]

# append
myList = [1,2,3,4,5]
myList.append(6)
print(myList) # [1, 2, 3, 4, 5, 6]

# word
myList = 'casa'
myList = list(myList)
print(myList) #['c', 'a', 's', 'a']
print(''.join(myList)) # casa