DELIMITER = ";"

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

def showData(Pdata:list[TIMESTAMP]):
    """Prints out the timestamps in required format"""
    print ("Electricity usage:")
    for i in range(len(Pdata)):
        print (f" - {Pdata[i].weekday} {Pdata[i].hour}:00, price {Pdata[i].price} €, consumption {Pdata[i].kWh} kWh, total {(Pdata[i].kWh * Pdata[i].price):.2f} €")
    return None

def main():
    print ("Program starting")
    csvData:list[TIMESTAMP] = []
    filename = input("Insert filename: ")
    readCsv(filename, csvData)
    showData(csvData)
    print ("Program ending.")
    return None

if __name__ == "__main__":
    main() 