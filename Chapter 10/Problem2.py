import math
class Calculator:
    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f"The square is {math.pow(n,2)}")
        print(f"The cube is {math.pow(n,3)}")
        print(f"The square root of this number {math.sqrt(n)}")

n=int(input("Enter the number: "))
a = Calculator(n)
a.square()