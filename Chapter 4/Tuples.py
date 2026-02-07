a = (1,2,5,6)
print(type(a)) #This will print <class 'tuple'> 

'''Tuples are similar to lists, but they are immutable, which means 
that you cannot change the values in a tuple after it has been created. 
Tuples are defined using parentheses () and the values are separated by 
commas.Lets write a tuple with one element:'''

b = (1)
print(type(b)) #This will print <class 'int'>
'''Well the data type of b will be int, not tuple. This is because the 
interpreter does not recognize it as a tuple since it does not
have any other element to distinguish it from a regular integer.'''

'''If we want to write such a tuple that contains only one element,
we need to include a comma after the element to indicate that it
is a tuple. For example:'''

single_tuple =(5, ) #This is a tuple with one element
print(type(single_tuple)) #This will print <class 'tuple'>

'''A tuple can also be created without using parentheses,
by simply separating the values with commas. For example:'''

c = 1,2,3,4
print(type(c)) #This will print <class 'tuple'>

'''A tuple can contain elements of different data types, 
just like a list. For example:'''

d = ('Apple', 3.14, True, [1,2,3], (4,5,6))
print(d) #This will print the tuple with different data types

'''Here we can seee a tuple can contain a list, another tuple,
bool, int, string and float. However, we cannot change the elements 
of a tuple after it has been created. If we try to change an
element of a tuple, we will get an error. For example:'''

try:
    d[0] = 'Mango' #This will raise a TypeError since tuples are immutable
except TypeError as e:
    print(e) #This will print the error message
