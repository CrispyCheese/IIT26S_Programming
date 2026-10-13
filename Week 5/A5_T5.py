def Options():
    Word = ""
    Menu = "Options:\n1 - Insert word\n2 - Show current word\n3 - Show current word in reverse\n0 - Exit"
    print (Menu)
    Feed = int(input("Your choice: "))
    while Feed != 0:
        if Feed == 1:
            Word = input("insert word: ")
            print (Menu)
        elif Feed == 2:
            print (f"Current word is: {Word}")
        elif Feed == 3:
            print (f"Word reversed - \"{Word[::-1]}\"")
        else:
            print ("Unknown option! try again.")
        print ("Options:\n1 - Insert word\n2 - Show current word\n3 - Show current word in reverse\n0 - Exit")
        Feed = int(input("Your choice: "))
    else:
        print ("Unknown option! try again.")
def main():
    print ("Program starting.")
    Options()
    return None
main()