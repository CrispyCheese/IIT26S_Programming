def showOptions():
    print ("Options:\n1 - Show count\n2 - Increase count\n3 - Reset count\n0 - Exit")
    return None

def askChoice() -> int:
    userChoice = input("Your choice: ") 
    if userChoice.isnumeric() == True:
        return int(userChoice)
    else:
        return 4

def main():
    print ("Program starting.")
    counter = 0
    while True:
        showOptions()
        choice = askChoice()
        if (choice == 0):
            print ("Exiting program\n")
            break
        elif (choice == 1):
            print (f"Current count - {counter}\n")
        elif (choice == 2):
            counter += 1
            print ("Count increased!\n")
        elif (choice == 3):
            counter = 0
            print ("Cleared count!\n")
        else:
            print ("Unknown choice!\n")
    print ("Program ending.")

main()