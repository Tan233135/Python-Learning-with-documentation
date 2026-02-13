'''Write a program to print multiplication table of a given number using for loop.'''

num = int(input("Enter the number you want the multiplication of:\t"))
for i in range(1,11):
    print(f"{num} x {i} =  ",num*i)

'''Write a program to greet all the person names stored in a list 'l' and which 
starts with S.'''

l = []
n=int(input("Enter the amount of names you want to store:\t"))
for i in range(n):
    l.append(input(f"Enter the name of {i+1}:\t"))

for i in range(n):
    if(l[i][0]=="S"):
        print(f"Good Morning, {l[i]}")