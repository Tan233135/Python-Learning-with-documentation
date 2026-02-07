'''Write a program that takes count the number of zeros in a tuple.'''

tuple1=()
x=int(input("Enter the number of elements in the tuple: "))
for i in range(x):
    element=int(input(f"Enter element {i+1}: "))
    tuple1+= (element,)

print(tuple1.count(0))