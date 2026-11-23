from template import numOptionsAndChoice
from time import sleep

def main():
    print ("Program starting.")
    pauseTime = float()
    while True:
        userChoice = numOptionsAndChoice("Set pause duration, Activate pause")
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
    print ("Program ending.")
    return None

if __name__ == "__main__":
    main()