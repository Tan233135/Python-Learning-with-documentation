'''Loops are used to repeat a block of code multiple times. In python,
there are two types of loops: for loops and while loops. 

For loops are used to iterate over a sequence (like a list, tuple, or
string or range) and execute a block of code for each item in the sequence.

while loops are used to execute a block of code as long as a certain condition is true.
'''

# For loop example
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

for char in 'hello':
    print(char)

for num in range(1,11):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# While loop example
count = 0
while (count < 5):
    print(count)
    count += 1