'''Variables are thought as a container for storing data values. 
In python, a variable is created the moment you first assign a value to it.
Unlike other programming languages, variable is actually a class in python.'''


a = 1   # a contains a integer value 
# In the RAM the location of the variable a is stored and the value 1 is assigned to it.


b = "Tanvir"   # b contains a string value
''' The variable b is assigned the value "Tanvir". You might think, How a word can be assigned as a variable?
In python, we can assign any type of data to a variable.
It can be a number, a list, a string, a single character,
a boolean value, a function, a class, an object, etc. 
The possibilites are endless....'''

c = 3.14    # c contains a float value

d = True    # d cointains a boolean value

e = None    # e contains a None value. It is used to represent the absence of a value or a null value.

''' Here, we have assigned different types of data to different variables.'''

print(a , b , c , d , e, sep = "\n") 

'''We can also print multiple variables with different data types 
in a sing print statemtent in python using commas(,).'''

print(type(a)) # the type() function prints the data type of the variable
print(type(b))
print(type(c))
print(type(d))
print(type(e))


'''<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'> 
<class 'NoneType'>

Here we can see the output. But the the type() function is returning a 
class type?? Does it mean the variable is a class?? How can a variable be a class??
Well, in python everything is an object. Even the data types are classes in python.
So, when we create a variable and assign a value to it, The variable becomes
an instance of that class. Hence, the type() function returns the class type 
of the variables.
'''
