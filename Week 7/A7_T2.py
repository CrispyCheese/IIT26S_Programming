def checkWrongInputs(Pinput:str, PintList:list[int]):
    """Splits the user input and checks for non integers adding valid integers into a list"""
    userInput = Pinput.split(",")
    for i in range(0, len(userInput)):
        if ((userInput[i]).isnumeric() != True):                     #Check if user input contains something else than numbers
            print (f"Invalid value \'{userInput[i]}\' detected.")                        
        else:
            PintList.append(int(userInput[i]))                        #Add the valid inputs into the list
    return None
       
def getSumandEven(Pnumberlist:list[int]):
    """Gets list containing integers sums them all and checks if sum is even or odd returns a string to be printed"""
    total = 0
    for i in range(0,len(Pnumberlist)):
        total += Pnumberlist[i]
    if ((total % 2) == 0):                      #Checking if sum is even or odd
        return (f"Sum of the integers is {total} and it's even")
    else:
        return (f"Sum of the integers is {total} and it's odd")

def main():
    print ("Program starting")
    integerList: list[int] = []
    feed = input("Insert comma separated integers: ")
    checkWrongInputs(feed, integerList)
    if (len(integerList) == 0):
        print ("No values to analyse.")
    else:
        print (f"There are {len(integerList)} integers in the list")
        print (getSumandEven(integerList))
    print ("Program ending.")
    return None

main()