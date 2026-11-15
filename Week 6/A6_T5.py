def readValues(Pfilename:str)-> list:
    """Read values from the file return them in a list"""
    data = list()
    file = open(Pfilename, "r", encoding="UTF-8")
    while True: 
        line = file.readline()
        if (len(line) == 0):        #If the line is empty stop the loop.
            break
        data.append(line.strip())   #Add the content the current line into the list.
    file.close()
    return data

def analyseValues(Pnumbers:list):
    """Gets a list of numbers as a parameter and performs analysis on them and returns the results in .csv formatted string"""
    numberCount = len(Pnumbers)
    totalSum = int()
    largestNum = int(Pnumbers[0])               #Initialise the largest number as the first one in the list
    for i in range(0,numberCount):              #Loop through the list to get the data for analysis
        totalSum += int(Pnumbers[i])            #Add the indexed number to the total.
        if (largestNum < int(Pnumbers[i])):     #Check if the number contained in list index i is larger than the currently largest.
            largestNum = int(Pnumbers[i])       #If true change the largest number to the one in list index i
    average = (totalSum / numberCount)
    header =  ("Count;Sum;Greatest;Average\n")
    return (header + str(numberCount) + ";" + str(totalSum) + ";" + str(largestNum) + ";" + "{:.2f}".format(average) + "\n")

def main ():
    print ("Program starting.")
    filename = input("Insert filename: ")
    numberList = readValues(filename)
    print ("### Number analysis - START ###")
    result = analyseValues(numberList)
    print (result)
    print ("#### Number analysis - END ####")
    print ("Program ending.")
    return None

main ()