'''Repeat Program 4 for a list of such words to be censored'''
words = ["Tanvir","Sami","Mishkat","Shuvo"]
with open("E:\python learning\Chapter 9\lists.txt","r") as f:
    content = f.read()


with open("E:\python learning\Chapter 9\lists.txt","w") as f:
    for i in range(len(words)):
        f.write(f"{content.replace(f"{words[i]}","#####")}")