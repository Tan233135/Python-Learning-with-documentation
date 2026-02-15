'''Functions in python are used to reduce the redundency of the code.
If a specefic task is required to be done multiple times, We can do it 
by making a function once and call the function whenever it's necessary.
This way we can reduce the codes redundancy and make the code efficient.

When we use a function it's called function "calling". When a function is
called, the function might or might not require an argument to be passed. 
Then using the argument or without the argument as the funciton is written,
it will complete a specefic task and return a output to wherever the function
is called.

We can also think of it as a maths function.

            f(x) = equation = output
'''

def average(s):
    a = sum(s)/len(s)
    return a

n = int(input("Enter the amount of number:\t"))
s = []
for i in range(n):
    s.append(int(input(f"Enter The {i+1} number:\t")))

ave=average(s)
print(ave)