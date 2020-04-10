# -*- coding: utf-8 -*-


def palindromeBig(word):
    reverseLetters = []
    for letter in word:
        reverseLetters.insert(0, letter)

    reverseWord = ''.join(reverseLetters)
    if word == reverseWord:
        return True
    return False

def palindromeSmall(word):
    reverseWord = word[::-1] # : Comienzo : Final : pasos -> Desde el inicio: hasta el final: invertido -1
    return word == reverseWord

def palindromeSuperSmall(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

def run():
    word = str(input('Get any word: '))
    response = palindromeBig(word)
    # First Example
    if response is True:
        print('The word {} is a Palindrome'.format(word))
    else:
        print('The word {} in NOT a Palindrome'.format(word))

    # Second Example
    if palindromeSmall(word) is True:
        print('The word {} is a Palindrome'.format(word))
    else:
        print('The word {} in NOT a Palindrome'.format(word))

    # Third Example
    if palindromeSuperSmall(word) is True:
        print('The word {} is a Palindrome'.format(word))
    else:
        print('The word {} in NOT a Palindrome'.format(word))

# Init software
if __name__ == "__main__":
    run()
