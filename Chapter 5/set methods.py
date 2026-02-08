s = {1,2,"Tanvir", (1,2)} #This is a set with different types of elements

s.add(6) #This will add 6 to the set
print(s)

'''we can also remove an element from the set using the remove() method.'''
s.remove(2) 
print(s)

'''We can also use the discard() method to remove an element from the set.
The difference between remove() and discard() is that remove() will raise an error
if the element is not found in the set, while discard() will not raise an error.'''
s.discard(3) #This will remove 3 from the set

'''We can also use the pop() method to remove and return an arbitrary element
from the set.'''
removed_element = s.pop() #This will remove and return an arbitrary element from the set
print(removed_element) #This will print the removed element
print(s)

'''The len() function can be used to get the number of elements in the set.'''
print(len(s)) #This will print the number of elements in the set

'''The clear() method can be used to remove all elements from the set.'''
s.clear() #This will remove all elements from the set
print(s) #This will print an empty set