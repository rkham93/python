
from MadLibs import madlibs
from GuessTheNumber import number_guesser
from HangMan import hangman
from SlotMachine import slot_machine

gameList = {
    "Guess the number": number_guesser,
    "Hang Man": hangman,
    "Mad Libs": madlibs,
    "Slot Machine": slot_machine,
}

if __name__ == "__main__":
    UserInfo = {}
    Name = input("Enter your name?\n")
    print("Hi {Name}, How are you?!".format(Name=Name.capitalize()))
    gameNames = list(gameList.keys())
    stringToDisplay=''
    for i in range(len(gameNames)):
        stringToDisplay+='\n{i}: {gameName}\n'.format(i=i+1,gameName=gameNames[i])

    userInput = int(
        input("Which game do you want to play?\n" +stringToDisplay
    ))
    userInput -= 1
    Game = gameNames[userInput]
    UserInfo["username"] = Name
    UserInfo["game played"] = Game
    print("You have chosen the game: {game}\n".format(game=gameNames[userInput]))
    gameList[gameNames[userInput]].main()