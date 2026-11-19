WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(Pfilename:str, Pdata:list[str]):
    file = open(Pfilename, 'r', encoding="UTF-8")
    data = file.readlines()
    for i in range(len(data)):
        Pdata.append(data[i])
    file.close
    return None

def csvDataPrep(Pdata:list[str]):
    """Gets a .csv files content in a list removes the header row, newline characters and any empty rows"""
    Pdata.pop(0)                    #Remove header
    for i in range (len(Pdata)):
        Pdata[i].rstrip()           #Remove newline characters
        if (len(Pdata[i]) == 0):    #Check for empty rows
            Pdata.pop(i)            
    return None

def analyseData(Pdata:list[str], Presult:list[str]):
    """Counts the number of timestamps per day in the .csv file """
    weekdayCount = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(Pdata)):                     
        dataOfRow = (Pdata[i]).split(";")           #Split the .csv format string into a list
        for j in range(len(WEEKDAYS)):              #Loop through the weekdays 
            if (dataOfRow[0] == WEEKDAYS[j]):       
                weekdayCount[j] += 1                #If a day stamp is found increase the corresponding counter
        dataOfRow.clear()
    for n in range(len(weekdayCount)):              #Loop through the counter list
        Presult.append(WEEKDAYS[n] + " " + str(weekdayCount[n]))    #Add strings with weekday and the amount of stamps into the result list
    return None

def showResults(Presults:list[str]):
    print ("### Timestamp analysis ###")
    for i in range(len(Presults)):
        print (f" - {Presults[i]} stamps")
    print ("### Timestamp analysis ###")
    return None

def main():
    print ("Program starting.")
    csvData: list[str] = []
    results: list[str] = []
    filename = input("Insert filename: ")
    print (f"Reading file\"{filename}\".")
    readFile(filename, csvData)
    csvDataPrep(csvData)
    print ("Analysing timestamps.")
    analyseData(csvData, results)
    print ("Displaying results.")
    showResults(results)
    csvData.clear()
    results.clear()
    print ("Program ending.")
    return None

if __name__ == "__main__":
    main() 