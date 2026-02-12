'''Write a program to find the greatest of four 
numbers entered by the user.'''
numberlist=[]
for i in range(4):
    numberlist.append(int(input(f"Enter number {i+1}:\t")))

greatest = max(numberlist)
print(f"The greatest number among {numberlist} is {greatest}.")

#This problem can also be solve using if-elif-else ladder:
numberlist=[]
for i in range(4):
    numberlist.append(int(input(f"Enter number {i+1}:\t")))

if numberlist[0]>numberlist[1] and numberlist[0]>numberlist[2] and numberlist[0]>numberlist[3]:
    greatest = numberlist[0]
elif numberlist[1]>numberlist[2] and numberlist[1]>numberlist[3]:
    greatest = numberlist[1]
elif numberlist[2]>numberlist[3]:
    greatest = numberlist[2]
else:
    greatest = numberlist[3]

print(f"The greatest number among {numberlist} is {greatest}.")