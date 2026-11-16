
def decipherROT13(Pcontent:str):
    decipheredContent = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    rot13 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    for i in range (0, len(Pcontent)):                 #Loop through the input list of words
        deciphered = ""
        toDecipher = str(Pcontent[i])                    
        for u in range (0, len(toDecipher)):           #Loop through all the characters in the indexed word
            if (toDecipher[u] in rot13):               #Check if character is one to be deciphered
                index = rot13.index(toDecipher[u])
                deciphered += alphabet[index]          #Add the corresponding character to deciphered
            else:
                deciphered += toDecipher[u]                 
        decipheredContent += deciphered
    return decipheredContent

def readFile(Pfilename:str) ->list:
    file = open(Pfilename, "r", encoding="UTF-8")
    lines = file.readlines()            #Reads all the lines in the file and saves them as a list
    file.close()
    return lines

def writeFile(Pcontent:str,Pfilename:str):
    file = open(Pfilename, 'w', encoding="UTF-8")
    file.write(Pcontent)    
    file.close()
    return None

def saveProgress(Pnext:str,Pfilename:str):
    file = open(Pfilename, 'a', encoding="UTF-8")
    file.write(Pnext)
    file.close()

def main ():
    print ("Travel starting.")
    locations = ("home", "Galba's palace", "Otho's palace", "Vitellius' palace", "Vespasian's palace")
    progress = readFile("player_progress.txt")
    status = str(progress[len(progress) -1]).strip().split(";")
    print (f"Currently at {locations[int(status[0])]}")
    print (f"Travelling to {locations[int(status[1])]}...\n...Arriving to the {locations[int(status[1])]}.")
    password = decipherROT13((status[2]))
    print (f"Passing the guard at the entrance.\n\"{password.title()}!\"")
    print ("Looking for the message in the palace...\nAh, there it is! Seems cryptic.")
    message = readFile(f"{status[1]}_{status[2]}.gkg")
    saveProgress(str(message[0]), "player_progress.txt")
    message.pop(0)
    print ("[Game] Progress autosaved!\nDeciphering Emperor's message...")
    emperorsMessage = decipherROT13("".join(message))
    writeFile(emperorsMessage, f"{int(status[1])}-{password}.txt")
    print ("Looks like I've got now the plain version copy of the Emperor's message.\nTime to leave...")
    print ("Travel ending.")

main ()