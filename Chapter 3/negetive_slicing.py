'''Negetive indexing ia also possible in python. In negative indexing,
the index starts from -1 to -length. The last character of the string
has the index -1, the second last character has the index -2, and so on.

Normal indexing:            0  1  2  3  4  5
                            ^  ^  ^  ^  ^  ^
                            |  |  |  |  |  |
                   NAME = " T  a  n  v  i  r "
                            ^  ^  ^  ^  ^  ^
                            |  |  |  |  |  |
negetive indexing:         -6 -5 -4 -3 -2 -1
'''

name = "Tanvir"
print(name[-4:-1]) # This will return "anvi" as the last index is not included
print(name[-6:-1]) # This will return "Tanvi" as the last index is not included
print(name[-6:]) # This will return "Tanvir" as the last index is not included and we didn't specified the last index