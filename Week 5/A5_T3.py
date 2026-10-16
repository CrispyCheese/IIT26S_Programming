def main():
    print ("Program starting.")
    name = askName()
    greetUser(name)
    print ("Program ending.")
    return None

def askName():
    name = input("Insert name: ")
    return name

def greetUser(PName):
    print (f"Hello {PName}!")
    return None

main()