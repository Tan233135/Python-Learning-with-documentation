'''List is a container that holds a set of values of
any data type. It is a mutable data structure, 
Which means that you can change the values in a 
list after it has been created. Lists are
defined using square brackets [] and the values 
are separated by commas.'''

# Example of a list
my_list = ['Apple', 'Banana', 'Tanvir', 3, 2.56, True, "Mishkat"]

print(my_list) #We can print the whole list at once

'''We can also access individual elements of the
list using their index. The index starts at once.'''

print(my_list[0]) #This will print the first element of the list
print(my_list[6]) #This will print the seventh element of the list

'''We can also access a range of elements from a list
using slicing. The syntax for slicing is 
list[start:stop:step]'''
print(my_list[0:3]) #This will print the first three elements of the list
print(my_list[0:6:2]) #This will print every second element from the first six elements of the list

'''We can access the elements of a list in reverse
order using the negative index. The index -1 refers
to the last element of the list, -2 refers to the 
second last element, and so on.'''
print(my_list[-1]) #This will print the last element of the listr

'''We can change the elements of a list by 
assigning a new value to a specific index.'''
my_list[0] = 'Mango' #This will change the first element of the list to 'Mango'
print(my_list) #This will print the updated list


'''We can also check if an element is present in a list'''
print("Mango" in my_list)

'''A list can contain another list as an element, which is called
a nested list. We can access the elements of a nested list
using multiple indices. For example:'''
nested_list = [1, 2, [3, 4, 5], 6]
print(nested_list[2]) #This will print the nested list [3, 4, 5]
print(nested_list[2][0]) #This will print the first element of the nested list, which is 3

'''A list can also contain a tuple as an element. 
we can access the elements of the tuple using multiple indices
as well. For example:'''
list_with_tuple = [1, 2, (3, 4, 5), 6]
print(list_with_tuple[2]) #This will print the tuple (3, 4, 5)
print(list_with_tuple[2][0]) #This will print the first element of the tuple, which is 3

'''If a list contains another list and a tuple as elements,
we can access the elements of both the nested list and the tuple 
using multiple indices. For example:'''
complex_list = [1, 2, [3, 4, 5], (6, 7, 8), 9]
print(complex_list[2]) #This will print the nested list [3, 4, 5]
print(complex_list[3]) #This will print the tuple (6, 7, 8)
print(complex_list[2][0]) #This will print the first element of the nested list, which is 3
print(complex_list[3][0]) #This will print the first element of the tuple, which is 6
