'''Write a python program to display a user entered name
followed by Good Afternoon using input() function.'''

'''This solution can be done in three ways.'''

'''The firs method is to take the name as input and then
printing the name followed by Good Afternoon.'''
name = input("Enter your name: ")
print(f"Good Afternoon {name}")

'''The second method is to directly take the name as input
while printing the statement.'''
print(f"Good Afternoon {input('Enter your name: ')}")

'''The third method is to use concatenation to combine the
input string with the rest of the statement.'''
name = input("Enter your name: ")
Good = "Good Afternoon "
print(Good + name)
