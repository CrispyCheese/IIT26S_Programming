DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

class TIMESTAMP:
    weekday = ""
    hour = int()
    kWh = int()
    price = float()

def readCsv(Pfilename:str, Plist:list[TIMESTAMP]):
    """Read a .csv file filter out header and empty lines and build TIMESTAMPs of the rest into the timestamp list"""
    print (f"Reading file \"{Pfilename}\".")
    file = open(Pfilename, 'r', encoding="UTF-8")
    data = file.readlines()
    for i in range(1, len(data)):               #Loop through the data skipping the header row
        row = data[i].rstrip()                  
        if (len(row) == 0):                     #If the row is empty skip it
            continue
        tempList = row.split(DELIMITER)         
        timestamp = TIMESTAMP()                 #Build TIMESTAMPS
        timestamp.weekday = tempList[0]         #Weekday in the first column
        timestamp.hour = int(tempList[1])       #Hour in the second column
        timestamp.kWh = int(tempList[2])        #Power usage in the third column
        timestamp.price = float(tempList[3])    #Electricity price in the last column
        Plist.append(timestamp)                 #Add the filled TIMESTAMP into the list
    file.close()
    return None

def analyseDaily(Pdata:list[TIMESTAMP], Presults:list[str]):
    """Analyse the timestamp list and store the analysis in result list"""
    for i in range(len(WEEKDAYS)):                              #Loop through weekdays
        totalPower = 0
        totalCost = 0
        for j in range(len(Pdata)):                             #Loop through the hourly timestamps to collect daily data       
            if (Pdata[j].weekday != WEEKDAYS[i]):               #If not correct day, skip timestamp
                continue
            else:
                totalPower += Pdata[j].kWh                          #Gather the total daily electricity usage
                totalCost += (Pdata[j].kWh * Pdata[j].price)        #Gather the total daily electricity cost
        resultData = (f" - {WEEKDAYS[i]} usage {totalPower:.2f} kWh, cost {totalCost:.2f} €")
        Presults.append(resultData)
    return None

def main():
    print ("Program starting.")
    timestamps: list[TIMESTAMP] = []
    results: list[str] = []
    filename = input("Insert filename: ")
    readCsv(filename, timestamps)
    analyseDaily(timestamps, results)
    print ("Displaying results.")
    print ("### Electricity consumption summary ###")
    for i in range(len(results)):
        print (results[i])
    print ("### Electricity consumption summary ###")
    print ("Program ending.")
    return None

if __name__ == "__main__":
    main() 