'''Using else with a for loop allows us to execute
a block of code after the for loop has completed, but only
if the loop was not terminated by a break statement.'''

# For loop with else example
for i in range(5):
    print(i)

else:
    print("The for loop has completed without a break statement.")

# For loop with break statement
for i in range(5):
    if i==3:
        print("Breaking the loop at i=3")
        break
    print(i)
else:
    print("This else block will not be executed because the loop was terminated by a break statement.")