'''Now we will learn about some operations that we can perform on a dictionary.
Dictionaries are mutable, so we can change the values of existing keys, add new key-value pairs,
and remove key-value pairs from a dictionary.'''

'''We can change the value of an existing key by assigning a new value to that key. For example:'''
marks= {
    "Tanvir": 85,
    "Mishkat": 80,
    "Sabbir": 50
}
marks["Tanvir"] = 90 #This will change the value of the key "Tanvir" to 90
print(marks)

'''We can add a new key-value pair to the dictionary by assigning a value to a new key. For example:'''
marks["Sami"] = 70 #This will add a new key "Sami" with the value 70 to the dictionary
print(marks)

'''We can remove a key-value pair from the dictionary using the del keyword. For example:'''
del marks["Sabbir"] #This will remove the key "Sabbir" and its associated value from the dictionary
print(marks)

'''We can also use the pop() method to remove a key-value pair from the dictionary. This method takes the
 key as an argument and removes the key-value pair from the dictionary, returning the value associated with 
 the key. For example:'''
removed_value = marks.pop("Mishkat") #This will remove the key "Mishkat" and return its associated value, which is 80
print(marks) #This will print the updated dictionary after removing "Mishkat"
print(removed_value) #This will print the value that was removed, which is 80

'''We can also use the popitem() method to remove and return an arbitrary key-value pair from the dictionary.
This method is useful when we want to remove an item from the dictionary without knowing its key. For example:'''
removed_item = marks.popitem() #This will remove and return an arbitrary key-value pair from the dictionary
print(marks) #This will print the updated dictionary after removing an arbitrary key-value pair
print(removed_item) #This will print the key-value pair that was removed, which is a tuple containing the key and its associated value