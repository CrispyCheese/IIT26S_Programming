import template
from time import sleep

def main():
    print ("Program starting.")
    pauseTime = float()
    while True:
        template.showOptions("Set pause duration,Activate pause")
        userChoice = template.askChoice("Your choice", 2)
        if (userChoice == 0):
            print ("Exiting program\n")
            break
        elif (userChoice == 1):
            pauseTime = float(input("Insert pause duration (s): "))
            print ()
        elif (userChoice == 2):
            print (f"Pausing time for {pauseTime} seconds")
            sleep(pauseTime)
            print("Unpaused.\n")
        else:
            print (f"Unknown choice \"{userChoice}\"!")
    print ("Program ending.")
    return None

if __name__ == "__main__":
    main()