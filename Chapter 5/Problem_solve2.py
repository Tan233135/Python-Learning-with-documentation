'''Write a program to input eight number form the user
and display all the unique numbers once.'''

s=set()
for i in range(8):
    num=int(input(f"Enter number {i+1}: "))
    s.add(num)

print(f"Unique numbers: {s}")