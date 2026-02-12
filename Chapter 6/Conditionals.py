'''Conditionals are used to perform different
actions based on different conditions. In python, we use
if, elif and else statements to perform conditional operations.'''

# if statement
x=10
if x>5:
    print("x is grater than 5")
# if-else statement
y=3
if y>5:
    print("y is grater than 5")
else:
    print("y is less than or equal to 5")

# if-elif-else statement
z=7
if z>10:
    print("z is grater than 10")
elif z>5:
    print("z is grater than 5 but less than or equal to 10")
else:
    print("z is less than or equal to 5")

#Taking input from user to check for a condition:
age=int(input("Enter your age:\t"))
if age>=18:
    print("You are above the age of consent.")
    print("You can vote in elections.")
else:
    print("You are below the age of consent.")
