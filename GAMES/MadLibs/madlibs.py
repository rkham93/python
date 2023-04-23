import json

from utils import Print, delay, newLine

def setTheme():
    file=open("GAMES\MadLibs\Themes.json")
    Themes=json.load(file)
    ThemesList=list(Themes.keys())
    InputStatement='Please select a theme from the following:\n'
    for i in range(len(ThemesList)):
        InputStatement+=" {i}: {theme}\n".format(i=i+1,theme=ThemesList[i])
    Theme=input(InputStatement)
    Print('you have chosen the "{Theme}" Theme!'.format(Theme=ThemesList[int(Theme)-1]))
    newLine()
    return Themes[ThemesList[int(Theme)-1]]


def getBlanks(Story,innerBrace,outerBrace):
    innerBraceList=[]
    outerBraceletList=[]
    for i in range(len(Story)):
        
        if Story[i] == innerBrace:
            innerBraceList.append(i)
        elif Story[i]== outerBrace:
            outerBraceletList.append(i)
    Blanks=[]
    for i in range(len(innerBraceList)):
        Blanks.append(Story[innerBraceList[i]+1:outerBraceletList[i]])
    
    return Blanks

def MadLibs(Story,innerBrace,outerBrace):
    Blanks=getBlanks(Story,innerBrace,outerBrace)
    for Blank in Blanks:
        Line='Enter a {}: \n'.format(Blank)
        userInput=input(Line)     
        Story=Story.replace(innerBrace+Blank+outerBrace,'"'+userInput.capitalize()+'"',1)
    newLine()
    Print('Thanks for the inputs ...') 
    delay('small')
    newLine()
    Print('Generating your cool MadLibs !!!')    
    newLine()
    delay('large')
    Print(Story)

def main():
    theme=setTheme()
    innerBrace=theme["innerBrace"]
    outerBrace=theme["outerBrace"]
    Story=theme["Story"]
    MadLibs(Story,innerBrace,outerBrace)

if __name__ == "__main__":
    main()
 