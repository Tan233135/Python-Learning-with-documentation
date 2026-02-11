'''Write a code to check whether an age is grater than 
or equal to 18 and print the appropriate message.
'''
age=int(input("Enter your age:\t"))
if age>=18:
    print("You are above the age of consent.")
elif age<18 and age>0:
    print("You are below the age of consent.")
elif age<=0:
    print("Invalid age entered.")