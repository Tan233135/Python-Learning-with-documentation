'''Modes of opening a file
r - open for reading
w - open for writing
a - open for appending
+ - open for updating
"rb" will open for read in binary mode.
"rt" will open for read in text mode.'''

st = "Hey tanvir you are learning python"
f = open("file.txt","a")
f.write(st)
f.close() #Everytime we run this code due to the append mode a string will be added in the file