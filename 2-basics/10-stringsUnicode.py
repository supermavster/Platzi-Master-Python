# -*- coding: utf-8 -*-

# Immutable Strings
text = "nice" # normal string
#text[0] = "r" # Replace first element (n) of the string an change for "r"
# Error: the variable Strings are Immutable

# Examples
textOne = "lola"
textTwo = "Angel"

# Equals
print(textOne == textOne) # True Is the same type and value
print(textOne == textTwo)  # False 1) these elements are Strings but this data is different

# Size Strings
print(textOne > textTwo) # True: l is bigger than A (in ascii numeric value)
print(textOne < textTwo) # False:  A is smaller than l (in ascii numeric value)

print(len(textOne)) # Count elements or characters (not value ascii)
print(len(textTwo)) # Count elements or characters (not value ascii)

print(len(textOne) > len(textTwo)) # False: 4 > 5 - Count elements or characters (not value ascii)
print(len(textOne) < len(textTwo)) # True: 4 < 5 - Count elements or characters (not value ascii)