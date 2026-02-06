'''We can write strings in three ways. We can use 
single quotes, double quotes, or triple quotes.'''

# Using single quotes
string1 = 'Hello, World!'
print(string1)
# Using double quotes
string2 = "Hello, World!"
print(string2)
# Using triple quotes
string3 = '''Hello, world!'''
print(string3)

'''The triple quotes are also used for multi-line strings.'''

multi_line_string = '''This is a multi-line string.'''
print(multi_line_string)

'''In python strings are immutable, which means
that we can't change the value of a string once it is created.
If we want to change the value of a string, we have to create 
a new string with the desired value.'''

name = "Tanvir"

'''The index in a string start from 0 to (length - 1) in python.
In order to slice a string, we use the following syntax:

            sl=name[ind_start:ind_end]
                      ^         ^     
                      |         |     
      First index included   Last index not included 
      
such as:
            sl[0:3] returns "Tan"    --->  characters fro 0 to 3 (excluding 3)
            sl[1:3] returns "an"     ---> characters from 1 to 3 (excluding 3)
            sl[0:5] returns "Tanvi" ---> characters from 0 to 5 (excluding 5)'''

print(name[0:3])
print(name[1:3])
print(name[0:5])