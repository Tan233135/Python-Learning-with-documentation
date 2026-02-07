marks= {
    "Tanvir": 85,
    "Mishkat": 80,
    "Sabbir": 50,
    0: "Zero"
}

'''We will know about some of the methods of a dictionary.'''
'''The items() method returns a view object that displays a list of a dictionary's key-value pairs.'''
print(marks.items())

'''The keys() method returns a view object that displays a list of all the keys in the dictionary.'''
print(marks.keys())

'''The values() method returns a view object that displays a list of all the values in the dictionary.'''
print(marks.values())

'''The update() method updates the dictionary with the key-value pairs from another dictionary or from
 an iterable of key-value pairs.'''
marks.update({"Sami": 70, "Zihan": 90})
print(marks)

'''The get() method returns the value for a specified key if the key is in the dictionary. If the key is not found, it returns a default value (which is None if not specified).
For example:'''
print(marks.get("Tanvir")) #This will print 85 since the key "Tanvir" is in the dictionary

'''Whats the difference between using the get() method and accessing the value directly using the key?

The main difference is that if you try to access a key that does not exist in the dictionary using the 
get() method, it will return None (or a specified default value), whereas if you try to access a key that 
does not exist using the square bracket notation (marks["key"]), it will raise a KeyError. For example:'''
print(marks.get("NonExistentKey")) #This will print None since the key "NonExistentKey" is not in the dictionary
print(marks["NonExistentKey"]) #This will raise a KeyError since the key "NonExistentKey" is not in the dictionary

