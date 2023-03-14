from mad_libs import madlibs_main
from number_guesser import number_guesser_main

if __name__ =="__main__":
    userInput=input('Which game do you want to play?\n1.Mad Libs\n2.Number Guessing\n')
    if int(userInput)==1:
        madlibs_main.startGame()
    else:
        number_guesser_main.startGame()