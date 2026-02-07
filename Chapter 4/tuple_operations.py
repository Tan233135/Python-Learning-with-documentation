'''We will learn about some operations that we can perform on a tuple.
Since tuples are immutable, we cannot change the elements of a tuple
after it has been created. However, we can perform some
operations on tuples that do not modify the original tuple.'''

'''Concatenation: '''

tuple1=(1,2,3)
tuple2=(4,5,6)
new_tuple=tuple1+tuple2
print(new_tuple) #This will print (1, 2, 3, 4, 5, 6)

'''Repetition:'''
tuple1=(1,2,3)
new_tuple=tuple1*3
print(new_tuple) #This will print (1, 2, 3, 1, 2, 3, 1, 2, 3)

'''Membership Testing:'''
tuple1=(1,2,3,4,5)
print(3 in tuple1) #This will print True since 3 is an element of the tuple
print(6 in tuple1) #This will print False since 6 is not an element of the tuple

'''Iteration:'''
tuple1=(1,2,3,4,5)
for item in tuple1:
    print(item)
#This will print each element of the tuple on a new line

'''Packing and Unpacking:'''
#Packing
packed_tuple = 1, 2, 3, 4, 5
print(packed_tuple) #This will print (1, 2, 3, 4, 5)
#Unpacking
a, b, c, d, e = packed_tuple
print(a) #This will print 1
print(b) #This will print 2
print(c) #This will print 3
print(d) #This will print 4
print(e) #This will print 5
'''Here, we have packed the values 1, 2, 3, 4, and 5 into a tuple called packed_tuple.
Then, we unpacked the values from the tuple into individual variables a, b, c, d, and e.'''