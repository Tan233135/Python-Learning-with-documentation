name = "Tanvir"

'''We can use the skip value in slicing to skip characters in a string.
The syntax for slicing with skip value is:

                sl=name[ind_start:ind_end:skip_value]
                
such as:
                sl[0:5:2] returns "Tvr"  ---> characters from 0 to 5 (excluding 5) with a skip value of 2
                sl[0:5:3] returns "Tn"   ---> characters from 0 to 5 (excluding 5) with a skip value of 3
'''

print(name[0:5:2])

'''Advance slicing technique:

                sl=name[::skip_value]
such as:
                sl[::2] returns "Tvr"  ---> characters from 0 to end with a skip value of 2
                sl[::3] returns "Tn"   ---> characters from 0 to end with a skip value of 3
'''

print(name[::2])