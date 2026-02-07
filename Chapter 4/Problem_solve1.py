'''Write a program to store seven fruits in a list entered by the user.'''

a = []

for i in range(7):
    fruit = input(f"Enter the name of a fruit {i+1}: ")
    a.append(fruit)

print(a)