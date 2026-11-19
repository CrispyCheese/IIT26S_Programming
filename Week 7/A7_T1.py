def showIntegers(Pintegers:list):
    """Prints out the integer list"""
    print (f"Displaying {len(Pintegers)} integers.")
    for i in range(0, len(Pintegers)):
        print (f"- Index {i} => Ordinal {i + 1} => Integer {Pintegers[i]}")
    return None

def collectIntegers(PintList:list[int]):
    """Asks user to input integers and collects them in a list"""
    while True:
        feed = input("Insert positive integer(negative stops): ")
        if (feed.isnumeric() != True):      #If input is not numbers do nothing
            continue
        elif (int(feed) < 0):               #If input is empty stop loop
            break
        else:
            PintList.append(int(feed))      #Add input into the list as integer
    return None

def main():
    print ("Program starting.")
    print ("Collect positive integers.")
    posIntegers: list[int] = []
    collectIntegers(posIntegers)
    print ("Stopped collecting positive integers.")
    showIntegers(posIntegers)
    posIntegers.clear()
    print("Program ending.")
    return None

main()