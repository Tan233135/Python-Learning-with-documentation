'''Write a python function which converts inches to cms'''

def cm(inch):
    return 2.54*inch

inch=int(input("Enter length:\t"))
print(f"In CM: {cm(inch)}")