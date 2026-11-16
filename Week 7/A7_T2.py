def getIntList()->list:
    feed = input("Insert comma separated integers: ")
    return feed.split(",")

def checkWrongInputs(PintList:list)->list:
    """Gets list as input checks removes non integers from it and returns that list"""
    invalidIndexes = list()
    for i in range(0, len(PintList)):
        if (str(PintList[i]).isnumeric() != True):              #Check if user input contains something else than numbers
            print (f"Invalid value \'{PintList[i]}\' detected.")
            invalidIndexes.append(i)                                 #Save the index of invalid inputs
        else:
            PintList[i] = int(PintList[i])
    for u in range (0,len(invalidIndexes)):                     #Remove invalid inputs 
        PintList.pop(invalidIndexes[u])
    return PintList
        
def getSumandEven(Pnumberlist:list):
    """Gets list containing integers as input counts the sum of all and checks if the sum is even or odd returning corresponding string"""
    total = 0
    for i in range(0,len(Pnumberlist)):
        total += Pnumberlist[i]
    if ((total % 2) == 0):
        return (f"Sum of the integers is {total} and it's even")
    else:
        return (f"Sum of the integers is {total} and it's odd")

def main():
    print ("Program starting")
    integerList = getIntList()
    checkWrongInputs(integerList)
    if (len(integerList) == 0):
        print ("No values to analyse.")
    else:
        print (f"There are {len(integerList)} integers in the list")
        print (getSumandEven(integerList))
    print ("Program ending.")
    return None

main()