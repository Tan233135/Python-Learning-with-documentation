import os
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in '%s':%s"%(cwd,files))

f = open("file.txt")
data = f.read()
print(data)
f.close()