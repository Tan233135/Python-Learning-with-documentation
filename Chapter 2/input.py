a=input("Enter number 1: ")

'''In python we can take input from the user using 
the input() function. The input() function reads a line 
from the user, converts it into a string (stripping a trailing
newline), and returns that. The syntax of the input() function
is: input(prompt) where prompt is the string that is printed
to the user before taking input. In python the inputs are 
taken as string by default. If we want to take input in any
other data type. We have to explicitly convert the string input
to the desired data type using typecasting.'''


b=input("Enter number 2: ")

'''lets learn a hack. To copy a line multiple times,
we can use the "ALT + SHIFT + DOWN ARROW" shortcut in 
most code editors. This allows us to quickly duplicate a line'''

print(f"This is the string concatenation: {a+b}") #This will concatenate as the input is now in string

#The answer will be "12" as we didn't converted the input data type to integar.

#Now we will convert the input data type to int using int() function.

a = int(a)
b = int(b)
print(f"This is the mathematical sum: {a+b}") #This will now mathematically add the two numbers

# we can directly typecast the data type while taking input

a = int(input("Enter number 1: ")) 
b = int(input("Enter number 2: "))
print(f"This is also a mathematical sum: {a+b}")