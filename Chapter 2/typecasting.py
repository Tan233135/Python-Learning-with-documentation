'''Typecasting in python is the process of converting one data
type to another data type. It is also known as type conversion.
Typecasting is used to perform operations on variables of 
different data types. For example, if we want to add an integer 
and a float, we need to convert the integer to a float before
performing the addition. Typecasting can be done in two ways:
1. Implicit typecasting: It is done automatically by the python
interpreter. For example, when we add an integer and a float, 
the integer is automatically converted to a float.
2. Explicit typecasting: It is done manually by the programmer.
We can use the built-in functions to convert one data type to 
another data type. For example, we can use the int() function to
convert a float to an integer, or the str() function to convert 
an integer to a string.'''

# Example of implicit typecasting
a = 5       # integer
b = 2.5     # float
c = a + b   # a is implicitly converted to float
print(c)    # prints 7.5
print(type(c))  # prints <class 'float'>

# Example of explicit typecasting
x = 10.7    # float
y = int(x)  # explicitly converting float to integer
print(y)     # prints 10
print(type(y))  # prints <class 'int'>
z = 20      # integer
w = str(z)  # explicitly converting integer to string
print(w)     # prints '20'
print(type(w))  # prints <class 'str'>

# Converting string to float
s = "3.14"
f = float(s)  # explicitly converting string to float
print(f)      # prints 3.14
print(type(f))  # prints <class 'float'>

# Converting integer to string
n = 100
str_n = str(n)  # explicitly converting integer to string
print(str_n)     # prints '100'
print(type(str_n))  # prints <class 'str'>

# Converting string to integer
num_str = "50"
num_int = int(num_str)  # explicitly converting string to integer
print(num_int)      # prints 50
print(type(num_int))  # prints <class 'int'>

# Converting float to string
float_num = 9.81
str_float = str(float_num)  # explicitly converting float to string
print(str_float)      # prints '9.81'
print(type(str_float))  # prints <class 'str'>

# Converting string to boolean
bool_str = "True"
bool_val = bool(bool_str)  # explicitly converting string to boolean
print(bool_val)      # prints True
print(type(bool_val))  # prints <class 'bool'>

# Converting integer to float
int_num = 42
float_val = float(int_num)  # explicitly converting integer to float
print(float_val)      # prints 42.0
print(type(float_val))  # prints <class 'float'>

# Converting boolean to integer
bool_var = False
int_bool = int(bool_var)  # explicitly converting boolean to integer
print(int_bool)      # prints 0
print(type(int_bool))  # prints <class 'int'>

# Converting boolean to string
bool_value = True
str_bool = str(bool_value)  # explicitly converting boolean to string
print(str_bool)      # prints 'True'
print(type(str_bool))  # prints <class 'str'>

# Converting float to integer
float_value = 7.99
int_value = int(float_value)  # explicitly converting float to integer
print(int_value)      # prints 7
print(type(int_value))  # prints <class 'int'>

# Converting integer to boolean
int_value2 = 0
bool_value2 = bool(int_value2)  # explicitly converting integer to boolean
print(bool_value2)      # prints False
print(type(bool_value2))  # prints <class 'bool'>

# Converting float to boolean
float_value2 = 0.0
bool_value3 = bool(float_value2)  # explicitly converting float to boolean
print(bool_value3)      # prints False
print(type(bool_value3))  # prints <class 'bool'>

# Converting boolean to float
bool_value4 = True
float_value3 = float(bool_value4)  # explicitly converting boolean to float
print(float_value3)      # prints 1.0
print(type(float_value3))  # prints <class 'float'>

# Converting string to complex number
complex_str = "2+3j"
complex_num = complex(complex_str)  # explicitly converting string to complex number
print(complex_num)      # prints (2+3j)
print(type(complex_num))  # prints <class 'complex'>

# Converting complex number to string
complex_value = 4 + 5j
str_complex = str(complex_value)  # explicitly converting complex number to string
print(str_complex)      # prints '(4+5j)'
print(type(str_complex))  # prints <class 'str'>

# Converting integer to complex number
int_value3 = 6
complex_value2 = complex(int_value3)  # explicitly converting integer to complex number
print(complex_value2)      # prints (6+0j)
print(type(complex_value2))  # prints <class 'complex'>

# Converting float to complex number
float_value4 = 3.5
complex_value3 = complex(float_value4)  # explicitly converting float to complex number
print(complex_value3)      # prints (3.5+0j)
print(type(complex_value3))  # prints <class 'complex'>

# Converting complex number to float (only real part)
complex_value4 = 7 + 8j
float_value5 = float(complex_value4.real)  # explicitly converting real part of complex number to float
print(float_value5)      # prints 7.0
print(type(float_value5))  # prints <class 'float'>

# Converting complex number to integer (only real part)
complex_value5 = 9 + 10j
int_value4 = int(complex_value5.real)  # explicitly converting real part of complex number to integer
print(int_value4)      # prints 9
print(type(int_value4))  # prints <class 'int'>

#convertint complex number to float(only imaginary part)
complex_value6 = 11 +12j
int_value5 = float(complex_value6.imag)  # explicitly converting imaginary part of complex number to float
print(int_value5)      # prints 12.0
print(type(int_value5))  # prints <class 'float'>

# Converting complex number to integer (only imaginary part)
complex_value7 = 13 + 14j
int_value6 = int(complex_value7.imag)  # explicitly converting imaginary part of complex number to integer
print(int_value6)      # prints 14
print(type(int_value6))  # prints <class 'int'>

# Note: Direct conversion from complex to int or float is not allowed in Python.