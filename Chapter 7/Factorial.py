'''Write a program to calculate the factorial of a given number using for loop.'''

'''We know factorial is written like below:
                n!=n*(n-1)!
                n!=n*(n-1)*(n-2)*.......*1 so on till 1'''
import math
n=int(input("Enter a number to find its factorial:\t"))
print(f"The factorial of {n} is {math.factorial(n)}")

'''We can also do it using the for loop.'''
fact=1
for i in range(1,n+1):
    fact*=i

print(f"The factorial of {n} is {fact}")