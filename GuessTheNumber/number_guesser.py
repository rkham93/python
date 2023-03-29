"""
Number Guessing Game:
Rules:
User will be alloted 10 points at the start of the game.
For every incorrect guess, the user loses a point.  
"""
import random
import json
rangeStart=10
rangeEnd=20
winningNumber=random.randint(rangeStart,rangeEnd)


def addToScoreBoard(userName,score,turns):
    filename="GuessTheNumber\scoreboard.json"
    scoreCard={userName:{'score':score,'turns':turns}}
    with open(filename,'a') as file: 
        file.write(json.dumps(scoreCard,indent=4)+',')        
    print('Your new score has been added to the score board!')

def takeUserInput ():    
    return input("Please enter number between {rangeStart} & {rangeEnd}: ".format(rangeStart= rangeStart,rangeEnd=rangeEnd))

def main(userInput='',score=10,turns=1):

    userName=input("Please enter your name: ")
    while userInput!=winningNumber:
        userInput=takeUserInput ()
        if userInput.isnumeric():
            if int(userInput)==winningNumber:
                print("Yay!! you got it right!!")
                print("your score is {score} and it you {turns} turns to get it right!!".format(score=score, turns=turns))
                break
            elif int(userInput) not in range(rangeStart,rangeEnd):
                    print("this number is not in range {rangeStart} to {rangeEnd}".format(rangeStart=rangeStart,rangeEnd=rangeEnd)) 
                    score-=1
                    turns+=1
            else:
                score-=1
                turns+=1
                print("Thats not it! You lost a point.\nYour score is {score}: ".format(score=score))            
                if int(userInput)< winningNumber:
                    print("Go Higher!")
                elif int(userInput)> winningNumber:
                    print("Go Lower!")
        else:
            print("That wasn't a number")
    addToScoreBoard(userName,score,turns)

if __name__ =="__main__":
    main()