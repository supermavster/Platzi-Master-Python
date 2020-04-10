# -*- codign: utf-8 -*-
import random

def run():
    abc = {}
    lowerCase = { "min": 97, "max": 122}
    upperCase = { "min": 65, "max": 90}
    for element in range(lowerCase['min'], lowerCase['max']):
        abc[str(chr(element))] = str(chr(element + 2))

    for element in range(upperCase['min'], upperCase['max']):
        abc[str(chr(element))] = str(chr(element + 4))

    message = str(input("Get a message to encrypt:\n"))
    crypt = encrypt(message, abc)
    decry = decrypt(crypt, abc)
    print("El mensaje es '{}', donde se cifro de la siguiente manera '{}', \n Diccionario: \n{}".format(decry, crypt, abc))

def encrypt(message, abc):
    words = message.split(" ") # Break in each space a new element in array
    crypt = list()
    for word in words:
        cypherWord = ''
        for letter in word:
            cypherWord += abc[letter]
        
        crypt.append(cypherWord)
    return ' '.join(crypt)

def decrypt(message, abc):
    words = message.split(" ") # Break in each space a new element in array
    decrypt = list()
    for word in words:
        cypherWord = ''
        for letter in word:    
            for key, value in abc.items(): 
                if value == letter:
                    cypherWord += (key)
        decrypt.append(cypherWord)
    return ' '.join(decrypt)

if __name__ == "__main__":
    run()