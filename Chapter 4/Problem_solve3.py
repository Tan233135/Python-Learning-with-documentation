'''Write a program to sum a list with 4 numbers.'''

numbers = []

for i in range(4):
    num=int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print(sum(numbers))