'''Write a code to find whether a given number is prime or not.'''

'''This problem is very important as prime number checking is 
required in internet security, HTTPS servers, tokens, keys etc.
This problem can be solved in many different ways. Such as:
1. Seive of eratosthenes
2.Trivial checking O(n)
3.SQRT(n) prime checking O(sqrt(n))

For today the best possible solution with 100 correction rate
for 64 bits integers with fixed bases is Miller-Rabin primilty test, 
developed by Gary Miller and Michael Rabin.

For now we will only learn about the SQRT(n) 
permiability test.'''

import math      #Importing the math library to square root the number

def is_prime(n): #Primility check function
    if n<=1:           #a number which is less than or equal to 1 is not a prime number
        return False
    
    for i in range(2, int(math.sqrt(n))+1):  #a number which can be devided by any number between 2 to the int(sqrt) of that number has multiple divisors other than 1 or itself. Thus not prime
        if n%i==0:           #Checks for any divisor between the range of 2 to the int(sqrt(n))
            return False
    
    return True  #Any number which doesn't fulltill the conditions above has only two divisors 1 and itself. Thus prime

n=int(input("Enter the number to check permiablity:\t"))    #Taking input from user
if(is_prime(n)):                 #Calling the is_prime(n) function for primility test
    print("Prime")               #If the function returns true than its a prime number
else:
    print("Not Prime")          #Else if not True means False than its not a prime