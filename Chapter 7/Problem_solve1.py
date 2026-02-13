'''Write a program to find the sum of first n natural numbers using while loop'''

'''We can solve this by using the basic formula of

            sum of n = (n*(n+1))/2
'''
n=int(input("Enter the number to find the sum of n numbers:\t"))
print(f"The sum of {n} number is: {int((n*(n+1))/2)}")

'''We can solve this using a while loop also.'''
summation=0
for i in range(n+1):
    summation+=i

print(f"The summation of {n} number is:  {summation}")

'''We can also solve this also using the while loop.'''
summation1=0
i=0
while(i<=n):
    summation1+=i
    i+=1

print(f"The summation1 of {n} is: {summation}")