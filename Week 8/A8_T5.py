import hashlib
import template

FILENAME = "credentials.txt"
DELIMITER = ";"

def checkLogin(Pfilename:str, PuserData:list):
    file = open(Pfilename, 'r', encoding="UTF-8")
    users = file.readlines()
    for i in range(len(users)):
        if (PuserData[0] in users[i]):
            PuserData.append(users[i])
            if (hashlib.md5(bytes(PuserData[1], encoding="utf-8")).hexdigest() in users[i]):
                PuserData.append(True)
            else:
                PuserData.append(False)
    if (len(PuserData) == 2):
        PuserData.append(False)
        PuserData.append(False)
    file.close()
    return None

def addUser(Pfilename:str, PnameAndPW:list):
    file = open(Pfilename, 'r+', encoding="UTF-8")
    users = file.readlines()
    users.append(f"{len(users)};{PnameAndPW[0]};{hashlib.md5(bytes(PnameAndPW[1], encoding="utf-8")).hexdigest()}\n")
    file.seek(0)
    file.writelines(users)
    file.close()
    users.clear()
    return None

def changePW(Pfilename:str, PprofileData:str)->str:
    userProfile = PprofileData.split(DELIMITER)
    userProfile[2] = hashlib.md5(bytes(input("Insert new password: "), encoding="utf-8")).hexdigest() + "\n"
    file = open(Pfilename, "r+", encoding="utf-8")
    users = file.readlines()
    users[int(userProfile[0])] = ";".join(userProfile)
    file.seek(0)
    file.writelines(users)
    file.close()
    return (";".join(userProfile))

def getProfileInfo(PprofileData:str)->str:
    data = PprofileData.split(DELIMITER)
    return (data[0] + " - " + data[1])

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
            userData = []
            userData.append(input("Insert username: "))
            userData.append(input("Insert password: "))
            userData.append(checkLogin(FILENAME, userData))
            if (userData[3] == True):
                print ("Authentication successful!\n")
                while True:
                    template.showOptions("View profile,Change password")
                    loggedInChoice = template.askChoice("Your choice", 2)
                    if (loggedInChoice == 0):
                        print ("Logging out\n")
                        break
                    elif (loggedInChoice < 0 or loggedInChoice > 2):
                        print (f"Unknown choice \"{loggedInChoice}\"!\n")
                    elif (loggedInChoice == 1):
                        print (f"Profile ID {getProfileInfo(userData[2])}\n")
                    elif (loggedInChoice == 2):
                        userData[1] = changePW(FILENAME, userData[2])
                        print ("Password changed!\n")
                userData.clear()
            else:
                print ("Authentication failed!\n")
                userData.clear()
        elif (userChoice == 2):
            registerInfo = []
            registerInfo.append(input("Insert username: "))
            registerInfo.append(input("Insert password"))
            addUser(FILENAME, registerInfo)
            registerInfo.clear()
            print ("User registration completed!\n")

    print ("Program ending.")

if __name__ == "__main__":
    main() 