'''Write a program to find out whether a student has passed or failed
if it requires a total of 40% and least 33% in each subject
to pass. Assume 3 subjects and take marks as an input from the user.'''

marks=[]
for i in range(3):
    marks.append(int(input(f"Enter marks for subject {i+1}:\t")))

total_marks=sum(marks)
percentage=(total_marks/300)*100
if percentage>=40 and all(mark>=33 for mark in marks):
    print(f"Congratulations! You have passed with {percentage:.2f}%")
else:
    print(f"Sorry! You have failed with {percentage:.2f}%")