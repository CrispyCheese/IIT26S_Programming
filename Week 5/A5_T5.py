def optionsAndChoice():
    """Prints the options and returns users choice as an integer."""
    print ("Options:\n1 - Insert word\n2 - Show current word\n3 - Show current word in reverse\n0 - Exit")
    choice = int(input("Your choice: "))
    return choice

def main():
    print ("Program starting.")
    word = ""
    while True:
        userChoice = optionsAndChoice()
        if (userChoice == 0):
            print ("Exiting program.\n")
            break
        elif (userChoice == 1):
            word = input("Insert word: ")
            print ()
        elif (userChoice == 2):
            print (f"Current word - \"{word}\"\n")
        elif (userChoice == 3):
            print (f"Word reversed - \"{word[::-1]}\"\n")
        else:
            print ("Unknown option! try again.\n")
    print ("Program ending.")
    return None

main()