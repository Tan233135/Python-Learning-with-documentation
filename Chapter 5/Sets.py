'''Set is also a data structure in python. It is an unordered
collection of items. Every element is unique (no duplicates) 
and must be immutable (cannot be changed). However, a set 
itself is mutable. We can add or remove items from it. 
The set class in python is based on the mathematical concept 
of a set. It is a collection of distinct objects,
considered as an object in its own right.'''

s = set() #This is an empty set

s = {1,2,3,4,5} #This is a set with some elements

print(s,type(s)) #This will print the set and its type

s = {1,2,3, "Tanvir", (1,2)} #This is a set with different types of elements

'''The properties of a set are:

1. Sets are unordered
2. sets are unindexed
3. sets are mutable
4. There is no way to change items in sets
5. sets cannot contain duplicate values.'''