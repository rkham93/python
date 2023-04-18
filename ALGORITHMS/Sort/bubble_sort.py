from random import randint
array_length=5
min=10
max=100
arrayToBeSorted=[]
for i in range(array_length):
    arrayToBeSorted.append(randint(min,max))
print("Array to be sorted")
print(arrayToBeSorted)

def swapElements(array,index1,index2):
    placeholder=array[index2]
    array[index2]=array[index1]
    array[index1]=placeholder
    return array

def bubble(array):
    swap=True
    steps=len(array)-2
    for step in range(steps):
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                swapElements(array,i,i+1)
                print(i,array)
            swap=True


                
               
    
def maxFinder(array):
    max_val=array[0]
    for i in range(len(array)):
        if max_val<array[i]:
            max_val=array[i]
    return max_val

def minFinder(array):
    min_val=array[0]
    for i in range(len(array)):
        if min_val>array[i]:
            min_val=array[i]
    return min_val

def selection(array):
    steps=range(len(array)-1)
    j=0
    for step in steps:
        print("step: "+str(step))
        for i in range(len(array)-1):
            min_val=minFinder(array[j:])
            swapElements(array,array.index(min_val),j)
            print(array)
            j+=1

print("bubble sorting")
print(bubble(arrayToBeSorted))

# print("selection sorting")
# print(selection(arrayToBeSorted))
