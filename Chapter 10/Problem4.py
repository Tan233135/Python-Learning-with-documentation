import math
class Calculator:
    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f"The square is {math.pow(self.n,2)}")
    
    def cube(self):
        print(f"The cube is {math.pow(self.n,3)}")
    
    def sqrt(self):
        print(f"The squareroot is {math.sqrt(self.n)}")
    
    @staticmethod
    def hello():
        print("Hello there!")

x = int(input("Enter the number: "))
a = Calculator(x)
a.hello()
a.square()
a.cube()
a.sqrt()