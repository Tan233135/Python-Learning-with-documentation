'''We can also add new elements to a list using the
append() method. This method adds an element to the
end of the list.'''
my_list = ['Apple', 'Banana', 'Tanvir', 3, 2.56, True, "Mishkat"]
my_list.append('Orange')
print(my_list)

'''We can remove elements from a list using the remove() function.
This method removes the first occurrence of the specified element
from the list.'''
my_list.remove('Banana')
print(my_list)

'''We can also use the pop() method to remove an element
from a list. This method removes the element at the 
specified index and returns it. If no index
is specified, it removes and returns the last element
of the list.'''
print(my_list.pop(2))

'''The remove() and the pop() methods modifies the
original list. However, if we want to create a 
new list with the desired elements removed,
We can use the list comprehension technique.
For example, to create a new list without the 
element 'Apple', we can do the following: '''
new_list = [item for item in my_list if item != 'Apple']
print(new_list)

'''The 
"item for item in my_list if item!='Apple'" 

This line is a list comprehension that iterates through
each item in the original list(my_list) and including '''