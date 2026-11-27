import template
import datetime
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def readTimetamps(Pfilename:str, Pstamps:list[datetime.date])->None:
    file = open(Pfilename, 'r', encoding="UTF-8")
    data = file.readlines()
    for i in range(len(data)):
        line = data[i].rstrip()
        if (len(line) == 0):
            continue
        else:
            montDA = line.split("-")
            timestamp = datetime.date
    file.close()
    data.clear()
    return None

def main():
    stampList:list[datetime.date] = []
    print ("Program starting.")
    filename = input("Insert filenam: ")

    while True:
        template.showOptions("Calculate amount of timestamps during year,Calculate amount of timestamps during month,Calculate amount of timestamps during weekday")
        userChoice = template.askChoice("Your choice", 3)
        if (userChoice == 0):
            print ("Exiting program.\n")
            break
        elif (userChoice < 0 or userChoice > 3):
            print (f"Unknown choice \"{userChoice}\"!\n")
            continue
        elif (userChoice == 1):
            print ()
        elif (userChoice == 2):
            print ()
        elif (userChoice == 3):
            print ()
    print ("Program ending.")

if __name__ == "__main__":
    main() 