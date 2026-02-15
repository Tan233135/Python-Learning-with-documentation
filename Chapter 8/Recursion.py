'''Recursion is a way to go use a function as a self loop
to do a task and give the final answer.'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n=int(input("Enter a number:\t"))
print(f"The factorial of this number is:\t{factorial(n)}")