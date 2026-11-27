import hashlib
import template

FILENAME = "credentials.txt"
DELIMITER = ";"

def credentialPrompt()->list[str]:
    userInputs:list[str] = []
    userInputs.append(input("Insert username: "))
    userInputs.append(input("Insert password: "))
    return userInputs

def checkLogin(Pfilename:str, PnameAndPW:list[str])->bool:
    authSuccesful:bool = False
    file = open(Pfilename, 'r', encoding="UTF-8")
    users = file.readlines()
    for i in range(len(users)):
        if (PnameAndPW[0] in users[i]):
            if (hashlib.md5(bytes(PnameAndPW[1], encoding="utf-8")).hexdigest() in users[i]):
                authSuccesful = True
    return authSuccesful

def addUser(Pfilename:str, PnameAndPW:list):
    file = open(Pfilename, 'r+', encoding="UTF-8")
    users = file.readlines()
    users.append(f"{len(users)};{PnameAndPW[0]};{hashlib.md5(bytes(PnameAndPW[1], encoding="utf-8")).hexdigest()}\n")
    file.seek(0)
    file.writelines(users)
    users.clear()
    return None

def main():
    print ("Program starting.")
    while True:
        template.showOptions("Login,Register")
        userChoice = template.askChoice("Your choice", 2)
        if (userChoice == 0):
            print ("Exiting program.\n")
            break
        elif (userChoice < 0 or userChoice > 2):
            print (f"Unknown choice \"{userChoice}\"!\n")
            continue
        elif (userChoice == 1):
            nameAndPW = credentialPrompt()
            authorized = checkLogin(FILENAME, nameAndPW)
            if (authorized == True):
                print ("Authentication successful!\n")
            else:
                print ("Authentication failed!\n")
                nameAndPW.clear()
        elif (userChoice == 2):
            registerInfo = credentialPrompt()
            addUser(FILENAME, registerInfo)
            registerInfo.clear()
            print ("User registration completed!\n")

    print ("Program ending.")

if __name__ == "__main__":
    main() 