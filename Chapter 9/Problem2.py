'''The game() function in a program lets a user play a game 
and returns the score as an integer. You need to read a file "Hi-Score.txt" which is either 
blank or contains the previous Hi-Score. You need to write a program to update
the Hi-Score whenever the game() function breaks the Hi-Score.'''
import random
def game():
    print("You are playing the game..")
    score = random.randint(1,62)
    with open("E:\python learning\Chapter 9\hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!= ""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"Your score: {score}")
    if(score>hiscore or hiscore==""):
        with open("E:\python learning\Chapter 9\hiscore.txt","w") as f:
            f.write(str(score))

    return score

game()