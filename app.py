from MadLibs import madlibs
from GuessTheNumber import number_guesser
from HangMan import hangman

gameList={"Guess the number":number_guesser,"Hang Man":hangman,"Mad Libs":madlibs}

if __name__ =="__main__":
    UserInfo={}
    Name=input("Enter your name?\n")
    gameNames=list(gameList.keys())
    userInput=int(input('Which game do you want to play?\n'+"\n".join(gameNames))+'\n')
    Game=gameNames[userInput]
    UserInfo['username']=Name
    UserInfo['game played']=Game
    userInput-=1
    gameList[gameNames[userInput]].main()