import time

def clearLine(line):
    print ("\033[A"+ ' '*len(line) +"\033[A")

def addWhiteSpaces(String):
    return ' '+String+' '

def newLine(n=1):
    print('\n'*n)         
    
def Print(String):
    j,c,z,Length=0,0,0,100   
    for i in range(len(String)):
        if len(String[j:i])>Length:
            if String[i]==' ':
                z=i-((c+1)*Length)+1
                newLine()
                c+=1
            j=(c*Length)+z
        toPrint=String[j:i+1]
        clearLine(toPrint)
        print(toPrint)
        time.sleep(0.025)


def delay(delay_time='small',bufferSymbol = '<->'):
    startTime=time.time()
    if delay_time=='small':
        interval=1
    elif delay_time=='medium':
        interval=3
    elif delay_time=='large':
        interval=5
    elif type(delay_time)==int:
        interval=delay_time
    elif delay_time.isnumeric():
        interval=int(delay_time)
    
    while time.time() < startTime+interval:
        for i in range(5):
            line = addWhiteSpaces(bufferSymbol) *i
            print(line)
            time.sleep(0.25)            
            clearLine(line)
        i=0
