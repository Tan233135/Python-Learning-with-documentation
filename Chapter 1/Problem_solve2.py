import os                              #imports the OS module

directory_path = 'E:/python learning'  #specifies the directory path

contents =os.listdir(directory_path)   # Creates a list containing the files of the specified directory

print(contents)                        # prints the created list to the terminal