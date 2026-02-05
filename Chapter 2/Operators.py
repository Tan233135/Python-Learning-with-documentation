'''
We have all heard about operators in mathematics. In python, they are quite similar
and are used to do mathematical, logical, bitwise and other types of operations
on variables and values.

Arithmetic operators: +, -, *, /, //, %, **
Comparison operators: ==, !=, >, <, >=, <=
Logical operators: and, or, not
Assignment operators: =, +=, -=, *=, /=, //=, %=, **=
Bitwise operators: &, |, ^, ~, <<, >>
Membership operators: in, not in
Identity operators: is, is not

These are the basic operators in Python. There are also other operators like the ternary operator, but these are the most commonly used ones.'''

# Example of arithmetic operators
a = 10
b = 3
print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a // b) # floor division
print(a % b)  # modulus
print(a ** b) # exponentiation

#Example of comparison operators
print(a == b)  # equal to
print(a != b)  # not equal to
print(a > b)   # greater than
print(a < b)   # less than
print(a >= b)  # greater than or equal to
print(a <= b)  # less than or equal to

#Example of logical operators 
x = True
y = False
print(x and y)  # logical AND
print(x or y)   # logical OR
print(not x)    # logical NOT

#Example of assignment operators
c = 5
c += 2  # equivalent to c = c + 2
print(c)  # prints 7
c *= 3  # equivalent to c = c * 3
print(c)  # prints 21

#Example of bitwise operators
p = 5  # in binary: 0101
q = 3  # in binary: 0011
print(p & q)  # bitwise AND, result is 1 (0001 in binary)
print(p | q)  # bitwise OR, result is 7 (0111 in binary)
print(p ^ q)  # bitwise XOR, result is 6 (0110 in binary)
print(~p)     # bitwise NOT, result is -6 (in binary: 1010)
print(p << 1) # left shift, result is 10 (in binary: 1010)
print(p >> 1) # right shift, result is 2 (in binary: 0010)

#Example of membership operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # checks if 3 is in the list, returns True
print(6 not in my_list)  # checks if 6 is not in the list

#Example of identity operators
a = [1, 2, 3]
b = a  # b is assigned the same list as a
c = [1, 2, 3]  # c is a new list with the same content as a
print(a is b)  # checks if a and b are the same object, returns True
print(a is c)  # checks if a and c are the same object, returns False
print(a == c)  # checks if a and c have the same content, returns True

