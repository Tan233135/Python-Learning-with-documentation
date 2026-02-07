'''Now we will see the different methods that we can use
with tuples. Since tuples are immutable, they have fewer methods
compared to lists. However, there are still some useful methods
that we can use with tuples.'''
my_tuple = (1,2,3,4,5)

'''The count() method returns the number of times a specified
element appears in the tuple. For example:'''
print(my_tuple.count(2)) #This will print 1 since the element 2 appears once in the tuple

'''The index() method returns the index of the first occurrence
of a specified element in the tuple. For example:'''
print(my_tuple.index(3)) #This will print 2 since the element 3 is at index 2 in the tuple

'''The len() function can be used to get the number of elements
in a tuple. For example:'''
print(len(my_tuple)) #This will print 5 since there are 5 elements in the tuple

'''The max() and min() functions can be used to get the maximum
and minimum values in a tuple, respectively. For example:'''
print(max(my_tuple)) #This will print 5 since it is the maximum value in the tuple
print(min(my_tuple)) #This will print 1 since it is the minimum value in the tuple

'''The sum() function can be used to get the sum of all the
elements in a tuple. For example:'''
print(sum(my_tuple)) #This will print 15 since the sum of all the elements in the tuple is 15

'''The sorted() function can be used to get a sorted list of the
elements in a tuple. For example:'''
print(sorted(my_tuple)) #This will print [1, 2, 3, 4, 5] since the elements in the tuple are already sorted

'''The tuple() function can be used to convert a list into a tuple. For example:'''
my_list = [1,2,3,4,5]
my_tuple_from_list = tuple(my_list)
print(my_tuple_from_list) #This will print (1, 2, 3, 4, 5) since the list has been converted into a tuple

'''The zip() function can be used to combine two or more tuples into a single tuple of tuples. For example:'''
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped_tuple = zip(tuple1, tuple2)
print(tuple(zipped_tuple)) #This will print ((1, 'a'), (2, 'b'), (3, 'c')) since the two tuples have been combined into a single tuple of tuples

'''The enumerate() function can be used to get the index and value of each element in a tuple. For example:'''
my_tuple = ('Apple', 'Banana', 'Cherry')
enumerated_tuple = enumerate(my_tuple)
print(list(enumerated_tuple)) #This will print [(0, 'Apple'), (1, 'Banana'), (2, 'Cherry')] since the enumerate function returns a list of tuples containing the index and value of each element in the original tuple

'''The all() function can be used to check if all the elements in a tuple are true. For example:'''
my_tuple = (True, True, True)
print(all(my_tuple)) #This will print True since all the elements in the tuple are true
my_tuple = (True, False, True)
print(all(my_tuple)) #This will print False since not all the elements in the tuple are true

'''The any() function can be used to check if any of the elements in a tuple are true. For example:'''
my_tuple = (False, False, False)
print(any(my_tuple)) #This will print False since none of the elements in the tuple are true
my_tuple = (False, True, False)
print(any(my_tuple)) #This will print True since at least one of the elements in the tuple is true