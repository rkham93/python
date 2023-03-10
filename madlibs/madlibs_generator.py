
import time
def delay(delay_time):
    time.sleep(delay_time)

def newLine(n):
    print('\n'*n)         
    

def Print(String):    
    for i in range(len(String)+1):
        toPrint=String[0:i]
        print ("\033[A"+ ' '*len(toPrint) +"\033[A")
        print(toPrint)
        time.sleep(0.025)
        
def MadLibs(Story):
    Blanks=['place','noun','plural object','place','color','name of season']
    userInputs=[]
    for Blank in Blanks:
        userInput=input('Enter a {}: '.format(Blank))
        userInputs.append(userInput)
        Story=Story.replace('<'+Blank+'>','"'+userInput+'"',1)
    
    print('Thanks for the inputs ...') 
    newLine(1)
    delay(1)
    print('Please wait while we get your results ...')
    newLine(1)
    delay(1)
    print('The results are ready ...')
    newLine(1)
    delay(1)
    newLine(1)
    return Story

Story='I was on my way to the <place> yesterday, where I went to pick up <noun>, When I noticed that all the <plural object> near the <place> were <color>. It was <name of season> indeed.'
mablibs_generated=MadLibs(Story)
Print(mablibs_generated)