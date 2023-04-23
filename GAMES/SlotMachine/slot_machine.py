import json
import numpy as np

def getSymbols():
    pathToFile = "GAMES\SlotMachine\symbols.json"
    with open(pathToFile, "r") as file:
        jsonFile = json.loads(file.read())

        symbols = jsonFile["symbols"]
        columns = jsonFile["columns"]
        Verdict = jsonFile["Verdict"]
        return symbols, columns, Verdict


def getRandom(symbols):
    return np.random.randint(len(symbols) - 1)


def spin(symbols, columns):
    outArray = []
    for column in range(columns):
        outArray.append(symbols[getRandom(symbols)])

    countList = np.unique(outArray, return_counts=True)[1]
    print(outArray)

    if len(countList) == 1 and countList[0] == columns:
        return True
    else:
        return False


def closeGame():
    print("Exiting Game")


def main():
    symbols, columns, Verdict = getSymbols()
    print("Running initial spin!")
    while Verdict == False:
        Verdict = spin(symbols, columns)
        if Verdict == True:
            print("Yay! you won")
            break
        print("That wasn't the one! Wanna Spin again?")
        userInput = input()
        if userInput == "y":
            if Verdict == True:
                print("Yay! you won")
                closeGame()
                break
        elif userInput == "n":
            closeGame()
            break
        else:
            break


if __name__ == "__main__":
    main()
