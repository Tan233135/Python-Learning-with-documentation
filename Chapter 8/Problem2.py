'''Write a program using function to convert celsius to fahrenheight.'''
def faren(celcius):
    return (9*celcius/5)+32

temp=int(input("Enter the temperature:\t"))
print(f"The temperature in farenheight is: {faren(temp)}")