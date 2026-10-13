def main():
    print ("Program starting.")
    PName = askName()
    greetUser(PName)
    print ("Program ending.")
    return None

def askName():
    PName = input("Insert name: ")
    return PName

def greetUser(PName):
    print (f"Hello {PName}!")
    return None