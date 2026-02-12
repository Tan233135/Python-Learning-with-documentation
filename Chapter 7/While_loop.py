'''while loops are used to execute a block of code as long as a certain condition is true.
'''
# While loop example
count = 0
while (count < 5):
    print(count)
    count += 1

# Another example of while loop
num = 1
while (num<=10):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
    num += 1

'''We can use the while loop to create an infinite loop,
but we need to be careful with it as it can cause our program to
crash if we don't have a way to break out of it.'''

# Infinite loop example
#While True:
# Print("This is an infinite loop")

while True:
    user_input = input("Enter 'exit' to break the loop:\t")
    if user_input.lower() == 'exit':
        print("Exiting the loop...")
        break
    else:
        print(f"You entered: {user_input}")