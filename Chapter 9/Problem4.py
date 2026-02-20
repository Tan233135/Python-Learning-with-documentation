'''A file contains a word "Donkey" multiple times. You need to write a 
program which replace this word with ##### by updating the same file.'''
word = "Donkey"

with open("E:\python learning\Chapter 9\Donkey.txt","r") as f:
    content = f.read()

contentNew=content.replace("Donkey","#####")

with open("E:\python learning\Chapter 9\Donkey.txt","w") as f:
    f.write(contentNew)