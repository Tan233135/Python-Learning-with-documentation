'''Write a python function to remove a given word from a list and strip it at the same time.'''

def stridel(word,l):
    if word in l:
        l.remove(word)
        for i in range(len(l)):
            l=l[i].strip()
    return l

l=[]
n=int(input("Enter the length of the list:\t"))
for i in range(n):
    l.append(input("Enter: "))

word=input("Enter a word to remove:\t")

print(stridel(word,l))