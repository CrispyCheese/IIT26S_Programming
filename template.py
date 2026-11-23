
def showOptions(Poptions:str)->int:
    DELIMITER = ","
    options = Poptions.split(DELIMITER)
    print ("Options:")
    for i in range(len(options)):
        print (f"{i + 1} - {options[i]}")
    print ("0 - Exit program")
    while True:
        choice = input("Your choice: ")
        if (choice.isnumeric()):
            if (int(choice) >= 0):
                choice = int(choice)
                break
    return choice

def getIntegerChoice(Pquestion:str, PchoiceAmount:int)->int:
    if (len(Pquestion) == 0):
        try:
            num = int(input("Your choice: "))
            if (0 <= num <= PchoiceAmount):
                return num
        except ValueError:
            print (f"Unknown choice please input numbers 0-{PchoiceAmount}")
