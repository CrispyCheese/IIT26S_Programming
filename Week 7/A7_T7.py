ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def getConfig()->str:
    """Asks user to choose one of the 3 configs and verifies the input returns the config filename"""
    print ("Choose one of 3 configs")
    while True:
        feed = input("Input a number 1, 2 or 3: ")
        if (feed.isnumeric()):                              #Checking if non numbers in the input
            if (1 <= int(feed) <= 3):                       #Check if the input is one of the options
                config = (f"iconf{int(feed)}.txt")          #Make the filename string and end the loop
                break
    return config

def getPlugs():
    """Asks user if they want to use the plugboard"""
    choice = str()
    while True:                     #Loop until user input is valid
        feed = input("Insert plugs (y/n)?: ")
        if (feed.strip().lower() == "y"):
            choice = "with plugs"
            break
        elif (feed.strip().lower() == "n"):
            choice = "without plugs"
            break
    return choice

def readFile(Pfilename:str)->list[str]:
    file = open(Pfilename, 'r', encoding="UTF-8")
    content = file.readlines()
    file.close
    return content

def setupEnigma(Pconfig:str, PenigmaConfig:list[list[str]]):
    config = readFile(Pconfig)
    for i in range(0, 3):                                        #Loop through the rotor config lines
        PenigmaConfig.append(list((config[i].rstrip())[7:]))     #Remove newline character and "rotor:" part from the beginning of the rows
    PenigmaConfig.append(list((config[3].rstrip())[10:]))        #Remove newline character and "reflector:" part from the row
    config.clear()
    return None                                       #Return the reflector string list

def rotateRotors(Protors:list[int]):
    """Function that rotates the rotors of the enigma machine"""
    Protors[0] += 1                 #Rotate the first rotor    
    if (Protors[0] == 26):          #Check if rotor 1 has done full rotation
        Protors[1] += 1             #Rotate the second rotor
        Protors[0] = 0                  
    if (Protors[1] == 26):          #Check if rotor 2 has done full rotation
        Protors[2] += 1             #Rotate the third rotor
        Protors[1] = 0             
    if (Protors[2] == 26):          #Check if rotor 3 has done full rotation
        Protors[2] = 0          
    return None

def backRotorPass(Pindex:int, Pconfig:list[str], ProtorShift:int):
    """Encryption wheel logic when going back from reflector"""
    shiftedIndex = (Pindex + ProtorShift) % 26              #Shift the index if the rotor is not at starting position
    charIn = Pconfig[shiftedIndex]                          #Character in the wheel at shifted index
    indexOut = (ALPHABET.index(charIn) - ProtorShift) % 26  #Index of the output character
    return indexOut

def reflectorPass(Pindex:int, Preflectorconfig:list[str]):
    """Character shift at the reflector"""
    char = Preflectorconfig[Pindex]                         #Input character into reflector
    index = ALPHABET.index(char)                            #Index of the character out of reflector
    return index

def fwdRotorPass(Pindex:int, Pconfig:list[str], ProtorShift:int):
    """Encryption wheel logic when going towards the reflector"""
    shiftedIndex = (Pindex + ProtorShift) % 26              #Shift the index if the rotor is not at starting position
    charIn = ALPHABET[shiftedIndex]
    indexOut = (Pconfig.index(charIn) - ProtorShift) % 26   #Index of the output character
    return indexOut

def encryptChar(Pinput:str, PenigmaConfig:list[list[str]], Protors:list[int])->str:
    """Encrypts the input character according to the chosen enigma config"""
    index = ALPHABET.index(Pinput)                                  #Index of the input character in alphabet
    for i in range(0, 3):                                           #Loop through the rotors towards reflector
        index = fwdRotorPass(index, PenigmaConfig[i], Protors[i])    
    index = reflectorPass(index, PenigmaConfig[3])                  #Reflectors character shift            
    for j in range(2, -1, -1):                                      #Looping through ther rotors backwards from reflector
        index = backRotorPass(index, PenigmaConfig[j], Protors[j])
    return (ALPHABET[index])
    
def main():
    print ("Program starting")
    enigmaConfig:list[list[str]] = []            #List of string lists to contain the rotor and reflector configurations
    rotorPos:list[int] = [0, 0, 0]               #Rotor position list
    configFilename = getConfig()
    plugs = getPlugs()
    print (f"Enigma initializing {plugs}")
    setupEnigma(configFilename, enigmaConfig)    #Get the rotor and reflector configs into enigmaConfig
    print ("Enigma initialized.\n")
    while True:
        output = ""
        feed = input("Insert row (empty stops): ")
        if (len(feed) == 0):
            break
        else:
            for i in range(0,len(feed)):                    #Loop through the user input
                if (feed[i].capitalize() in ALPHABET):
                    rotateRotors(rotorPos)                  #Rotate the rotors before each character gets encrypted
                    lightBulb = encryptChar(feed[i].capitalize(), enigmaConfig, rotorPos)       #Encrypt the character
                    print (f"Character \"{feed[i].capitalize()}\" illuminated as \"{lightBulb}\"")
                    output += lightBulb
                else:
                    output += feed[i]                       #If indexed character is not in alphabet add it without change
        print (f"Converted row - \"{output}\"\n")
        for j in range(len(rotorPos)):          #Looping through rotorpositions and resetting them to 0
            rotorPos[j] = 0
    rotorPos.clear()
    enigmaConfig.clear()
    print ("\nProgram ending.")
    return None

if __name__ == "__main__":
    main() 