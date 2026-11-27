import template
def readValues(Pfilename:str, Pnumbers:list[float])->None:
    file = open(Pfilename, 'r', encoding="UTF-8")
    data = file.readlines()
    for i in range(len(data)):
        line = data[i].rstrip()
        if (len(line) == 0):
            continue
        else:
            Pnumbers.append(float(line))
    file.close()
    data.clear()
    return None

def valuesSum(Pnumbers:list[float])->float:
    total = float()
    for i in range(len(Pnumbers)):
        total += Pnumbers[i]
    return total

def valuesAvg(Pnumbers:list[float])->float:
    total = float()
    for i in range(len(Pnumbers)):
        total += Pnumbers[i]
    average:float = total / len(Pnumbers)
    return average

def main():
    numList:list[float] = []
    filename = str()
    print ("Program starting.")
    while True:
        template.showOptions("Read values,Amount of values,Calculate sum of values,Calculate average of values")
        userChoice = template.askChoice("Your choice", 4)
        if (userChoice == 0):
            print ("Exiting program.\n")
            break
        elif (userChoice < 0 or userChoice > 4):
            print (f"Unknown choice \"{userChoice}\"\n")
            continue
        elif (userChoice == 1):
            filename = input("Insert filename: ")
            numList.clear()
            readValues(filename, numList)
            print ()
        elif (userChoice == 2):
            print (f"Amount of values {len(numList)}")
        elif (userChoice == 3):
            print (f"Sum of values {valuesSum(numList):.1f}\n")
        elif (userChoice == 4):
            print (f"Average of values {valuesAvg(numList):.1f}\n")
    numList.clear
    print ("Program ending.")

if __name__ == "__main__":
    main() 