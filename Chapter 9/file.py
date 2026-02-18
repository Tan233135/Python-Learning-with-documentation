'''
a = "a very long string with emails."
emails=[]

The random-access memory is volatile, and all contents are lost once a 
program terminates in order to persist the data forever, we use files.
A file is data stored in a storage device. A python program can talk to 
the file by reading content from it and writing content to it.

RAM=Volatile(temporary memory storage)
HDD=Non Volatile (Permanent memory storage)
'''
'''There are 2 types of files:
         1. Text files(.txt,.c, etc)
         3. Binary files(.jpg, .dat, etc)'''

f = open("file.txt")
data = f.read()
print(data)
f.close()