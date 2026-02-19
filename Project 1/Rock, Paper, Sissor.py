import random

point={"comp":0,"play":0}

def comp():
    print("Computer achived a point")
    global point
    point["comp"]+=1
    point["play"]-=1
    return point

def play():
    print("Player achived a point")
    global point
    point["play"]+=1
    return point

def win_or_loose():
    global point
    if(point["comp"]==point["play"]):
       print("Draw")
    elif(point["comp"]>point["play"]):
       print(f"\nComputer Won by {point["comp"]-point["play"]} point.")
    else:
       print(f"\nPlayer won by {point["play"]-point["comp"]} point.")

print('''It is a simple text based ROCK, PAPER SISSOR game.
      
      Rules:    1.The player will give input rock, paper, sissor
                2. If the player types "exit". The game will end and scores will be shown.
                3. For each time computer achives a point the player will lose one
                   but the same is not applicable for the computer.''')
print("\nEnter ROCK or PAPER or SISSOR\nOr type 'EXIT'\n")
while(True):
    numbers = ["rock","paper","sissor"]
    computer = random.choice(numbers)
    player =input("Player:\t")
    player=player.lower()
    if(player=='exit'):
       print(f"\nComputer Score: {point["comp"]}\nPlayer Score: {point["play"]}")
       win_or_loose()
       break
    elif(computer==player):
       print(computer)
       print("Draw")
       point["comp"]+=0
       point["play"]+=0
    elif(computer=="rock" and player=="sissor"):
       print(computer)
       comp()
    elif(computer=="rock" and player=="paper"):
       print(computer)
       play()
    elif(computer=="paper" and player=="rock"):
       print(computer)
       comp()
    elif(computer=="paper" and player=="sissor"):
       print(computer)
       play()
    elif(computer=="sissor" and player=="rock"):
       print(computer)
       play()
    elif(computer=="sissor" and player=="paper"):
       print(computer)
       comp()
    else:
       print("Invalid input. Try again.")