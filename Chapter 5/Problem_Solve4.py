'''Create an empty dictionary. Alllow 4 friends to enter their
facorite language as value and use key as their names. 
Assume that the names are unique.'''

empty_dict = {} #This is an empty dictionary
#Allowing 4 friends to enter their favorite language as value and using key as their names
'''Allowing 4 friends to enter their data using the input() function'''
for i in range(4):
    name=input(f"Enter the name of friend {i+1}:\t")
    language=input(f"Enter the Language of {name}:\t")
    empty_dict[name]=language

print(empty_dict) #This will print the dictionary with names as keys and favorite languages as values