print ("Program starting.\n")

StartNum = int(input("Insert starting point: "))
StopNum = int(input("Insert stopping point: "))
InspNum = int(input("Insert inspection point: "))

while True:
    if StartNum >= StopNum:
        print ("Starting point value must be less than the stopping point value.")
        print ("Inspection value must be within the range of start and stop.")
        break
    elif InspNum < StartNum or InspNum > StopNum:
        print ("Inspection value must be within the range of start and stop.")
        break
    else:
        print ("\nFirst loop - inspection with break:")
        for i in range(StartNum, StopNum):
            if (i == InspNum):
                break
            elif (i == InspNum -1):
                 print (i)
            else:
                 print (i, end=" ")
        print ("Second loop - inspection with continue:")
        for i in range(StartNum, StopNum):
            if (i == InspNum):
                continue
            elif (i == StopNum - 1):
                print (i)
            else:
                print (i, end=" ")
        break

print ("\nProgram ending.")