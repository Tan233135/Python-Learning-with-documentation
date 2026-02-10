'''Can you change the values inside a list which
is contained in set S = {8,7,"Harry", [1,2]}?'''

'''No, we cannot change the values inside a list which is contained in a set S = {8,7,"Harry", [1,2]}.
This is because sets in Python are unordered collections of unique elements, and they do not allow mutable 
elements like lists to be included as values. If we try to include a list in a set, we will get a TypeError 
because lists are mutable and cannot be hashed, which is a requirement for elements in a set.'''

S = {8,7,"Harry", [1,2]} #This will raise a TypeError because lists are mutable and cannot be hashed
print(S)