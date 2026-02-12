age=int(input("Enter your age:\t"))
#if statement no: 1
if (age%2==0):
    print("Your age is even.")
#if statement no: 2
if (age>=18):
    print("You are above the age of consent.")
elif (age<18 and age>0):
    print("You are below the age of consent.")
else:
    print("Invalid age entered.")

