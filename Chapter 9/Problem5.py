'''Repeat Program 4 for a list of such words to be censored'''
words = ["Tanvir","Sami","Mishkat","Shuvo"]
with open("E:\python learning\Chapter 9\lists.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#####")

with open("E:\python learning\Chapter 9\lists.txt","w") as f:
    f.write(content)