'''We will learn about dictionaries in python. A dictionary is a collection 
of key-value pairs. Each key is unique and maps to a value. 
Dictionaries are defined using curly braces {} and each key-value
pair is separated by a colon.
'''
# Example of a dictionary
marks= {
    "Tanvir": 85,
    "Mishkat": 80,
    "Sabbir": 50
}

print(marks, type(marks)) #This will print the dictionary and its type)

'''We can access the values in a dictionary using their keys.'''
print(marks["Tanvir"]) #This will print 85

random = {
    "name": "Tanvir",
    "age": 23,
    "is_student": True,
    "Friends": ["Mishkat", "Sami", "Zihan", "Shuvo"],
    "Marks": {"Math": 85, "Physics": 80, "Chemistry": 75},
    "Parents": ("Alauddin", "Roksana")
}

print(random["Friends"]) #This will print the list of friends
print(random["Marks"]) #This will print the dictionary of marks
print(random["Parents"]) #This will print the tuple of parents

'''Properties of a dictionary: 
1. it is unordered.
2. it is mutable.
3. it is indexed by keys.
4. Cannot contain duplicate keys.'''

