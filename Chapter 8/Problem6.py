'''Write a multiplication table of a given number using function'''

def multable(n):
    for i in range(1,11):
        print(f"{n} x {i}= {n*i}")

n=int(input("Enter the number:\t"))
multable(n)