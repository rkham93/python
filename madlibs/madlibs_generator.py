
import time
innerBrace='<'
outerBrace='>'
Story='I was on my way to the <place> yesterday, where I went to pick up <noun>, When I noticed that all the <plural object> near the <place> were <color>. It was <name of season> indeed.'
def loader():
    pass

def clearLine(line):
    print ("\033[A"+ ' '*len(line) +"\033[A")

def addWhiteSpaces(String):
    return ' '+String+' '

def delay(delay_time=1,bufferSymbol = '<->'):
    startTime=time.time()
    while time.time() < startTime+delay_time:
        for i in range(5):
            line = addWhiteSpaces(bufferSymbol) *i
            print(line)
            time.sleep(0.25)            
            clearLine(line)
        i=0

def newLine(n):
    print('\n'*n)         
    
def Print(String):    
    for i in range(len(String)+1):
        toPrint=String[0:i]
        clearLine(toPrint)
        print(toPrint)
        time.sleep(0.025)

def getBlanks(Story):
    chevronList=[]
    angleBraceletList=[]
    for i in range(len(Story)):
        
        if Story[i] == innerBrace:
            chevronList.append(i)
        elif Story[i]== outerBrace:
            angleBraceletList.append(i)

    Blanks=[]
    for i in range(len(chevronList)):
        Blanks.append(Story[chevronList[i]+1:angleBraceletList[i]])
    
    return Blanks

        
def MadLibs(Story):
    Blanks=getBlanks(Story)
    userInputs=[]
    for Blank in Blanks:
        userInput=input('Enter a {}: '.format(Blank))
        userInputs.append(userInput)
        Story=Story.replace(innerBrace+Blank+outerBrace,'"'+userInput.capitalize()+'"',1)
    
    print('Thanks for the inputs ...') 
    delay(2)
    print('Generating your cool MadLibs !!!')
    newLine(1)
    delay(5)
    
    return Story

mablibs_generated=MadLibs(Story)
Print(mablibs_generated)
