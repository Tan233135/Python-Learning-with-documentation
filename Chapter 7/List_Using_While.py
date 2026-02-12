'''Using while loop to iterate through a list is not
as common as using a for loop, but it can be done.
We can use a while loop to iterate through a list by
using an index to access each element in the list.'''

# Using while loop to iterate through a list
fruits = ['apple','banana','cherry']
index = 0
while (index < len(fruits)):
    print(fruits[index])
    index += 1