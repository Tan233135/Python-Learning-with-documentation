'''Write a program to accept marks fo 6 students and siplay them 
in a sorted manner.'''

marks = []
for i in range(6):
    mark=int(input(f"Enter the marks of student {i+1}: "))
    marks.append(mark)

marks.sort()
print("Marks of students in sorted manner: \n", marks)