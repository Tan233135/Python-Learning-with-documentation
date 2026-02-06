'''Calculate the square of a number. We can do this in two ways'''


'''The first method is to simply multiply the number by itself.'''
num = int(input("Enter a number: "))
print(f"The square of {num} using the first method is {num*num}")



'''The second method is to use the built-in pow() function. The
pow() function takes two arguments, the base and the exponent,
and returns the result of base raised to the power of exponent.
Though the pow() function returns a float value,
we can convert it to an integer using the int() function.'''
import math
print(f"The square of {num} using the second method is: {int(math.pow(num,2))}")