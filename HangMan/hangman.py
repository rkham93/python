word='strawberry'
wordLength=len(word)

def chancesCalculator(word):
    Dict={}
    room_for_error=3
    chances=len(word)+room_for_error

    for letter in word:
        letterCount=word.count(letter)
        if letterCount>1:
            Dict[letter]=letterCount

    chances-=sum(list(Dict.values()))
    return chances



def Blanks(wordLength):
    return '#'*wordLength
userGeneratedWord=Blanks(wordLength)

def makeList(Word):
    return list(Word)
userGeneratedWordList=makeList(userGeneratedWord)

def makeString(userGeneratedWordList):
    return ''.join(userGeneratedWordList)

def Validate(userGeneratedWordList,word):
    if makeString(userGeneratedWordList)==word:
        return True
    else:
        return False

def getIndexof(value,word):
    indexArray=[]
    for i in range(len(word)):
        if word[i]==value:
            indexArray.append(i)
    return indexArray
def showChancesLeft(chances):    
    print('You have {chances} left'.format(chances=chances))

def main():
    chances=chancesCalculator(word)
    print("your word has {wordLength} letters".format(wordLength=wordLength))
    print(userGeneratedWordList)
    while userGeneratedWord !=word and chances>0:
        userInput=input('input please: ')
        if userInput in userGeneratedWordList:
            print('you already used this letter. Try another one!')
            
        for element in getIndexof(userInput,word):
            userGeneratedWordList[element]=userInput
        chances-=1
        showChancesLeft(chances)
        print(userGeneratedWordList)
        

        if Validate(userGeneratedWordList,word):
            print('you have won')
            print('The word was : {word}'.format(word=word))
            break
    else:
        print("Out of chances to play!!")


if __name__=="__main__":
    main()