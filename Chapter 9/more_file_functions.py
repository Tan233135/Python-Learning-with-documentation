f=open("E:\python learning\Chapter 9\01File.txt")
lines=f.readline() #The readline() function returns a list of lines in the file
print(lines, type(lines))
while(lines!=""):
    print(lines)
    lines = f.readline()

f.close()