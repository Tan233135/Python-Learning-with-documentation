'''Write a python program to detect double space in a string.'''

string = input("Enter a string with double space: ")
print(string.find("  ") != -1)

'''It can also be done using the in operator.'''
print("  " in string)



'''Replacing the double space with single space in a string.'''
print(string.replace("  "," "))