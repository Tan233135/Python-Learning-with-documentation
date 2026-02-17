'''Write a program to find greatest of three numbers.'''

def greater(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

name1=int(input("Enter the 1'st number:\t"))
name2=int(input("Enter the 2nd number:\t"))
name3=int(input("Enter the 3rd number:\t"))

print(f"The greatest among them is: {greater(name1,name2,name3)}")