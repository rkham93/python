from MadLibs import madlibs
from GuessTheNumber import number_guesser
from HangMan import hangman

gameList={"Guess the number":number_guesser,"Hang Man":hangman,"Mad Libs":madlibs}
if __name__ =="__main__":
    userInput=int(input('Which game do you want to play?\n'+"\n".join(list(gameList.keys()))+'\n'))
    userInput-=1
    gameList[list(gameList.keys())[userInput]].main()