'''There are some functions of string operations in python.
We will discuss some of them here.'''

name = "tanvir"
print(len(name))

'''The len() function is used to find the length of a string.
The len() function returns the number of characters in a string,
including spaces.'''

'''Then thres endswith() function. It is used to check
whether a string ends with a specefic suffix or not.
The syntax for endswith() function is:
                string.endswith(suffix)
'''

print(name.endswith("vir"))

#This will return True or False based on the condition.

'''Similarly, theres startwith() function. It is used to check
whether a string starts with a specefic prefix or not.'''

print(name.startswith("Tan"))

#This will return True or False based on the condition.

'''Then there is capatilize() function. It is used to 
convert the first character of the first word of a string to uppercase
and the rest of the characters to lowercase.'''
print(name.capitalize())

'''The upper() function is used to convert all the characters
of a string to uppercase.'''
print(name.upper())

'''The lower() function is used to convert all the characters
of a string to lowercase.'''
print(name.lower())

'''The title() function is used to convert the first character of 
each word of a string to uppercase and the rest of the 
characters to lowercase.'''
print(name.title())

'''The swapcase() function is used to convert the uppercase characters
of a string to lowercase and the lowercase characters to uppercase.'''
print(name.swapcase())

'''The find() function is used to find the index of the first
occurrence of a substring in a string.'''
print(name.find("an"))


'''The replace() function is used to replace a substring with another
substring in a string.'''
print(name.replace("tan", "Tan"))


'''The strip() function is used to remove the leading and 
trailing whitespace characters from a string.'''
print(name.strip())

'''The split() function is used to split a string into a list 
of substrings based on a specified delimiter.'''
sentence = "Hello, World!"
print(sentence.split(", "))

'''The join() function is used to join a list of string into 
a single string with a specified delimiter.'''
words = ["Hello", "World"]
print(",".join(words))

'''The count() function is used to count the number of occurrences
of a substring in a string.'''
print(name.count("a"))