
def showOptions(Poptions:str)->None:
    DELIMITER = ","
    num = 0
    options = Poptions.split(DELIMITER)
    print ("Options:")
    for i in range(len(options)):
        print (f"{i + 1} - {options[i]}")
    print ("0 - Exit")
    
def askChoice(Pprompt:str, PchoiceAmount:int)->int:
    try:
        num = int(input(f"{Pprompt}: "))
    except ValueError:
        print (f"Unknown choice please input numbers 0-{PchoiceAmount}")
    return num
