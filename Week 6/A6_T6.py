def collectWords()->list:
    """Collects words from input returns them in a list"""
    words = list()
    while True:
        feed = input("Insert row(empty stops): ")
        if (len(feed) == 0):
            break
        else:
            words.append(feed)
    return words

def cipherWords(PwordList:list)->str:
    """Gets a list of words and performs rot13 cipher and returns ciphered words in a string"""
    cipheredContent = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    rot13 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    for i in range (0, len(PwordList)):                 #Loop through the input list of words
        ciphered = ""
        toCipher = str(PwordList[i])                    
        for u in range (0, len(toCipher)):              #Loop through all the characters in the indexed word
            for a in range(0,len(alphabet)):        #Find the index of the character in the alphabet variable
                if (toCipher[u] == alphabet[a]):
                    ciphered += rot13[a]            #Add the corresponding rot13 character to ciphered
                    break
                elif (a == (len(alphabet) -1)):
                    ciphered += toCipher[u]                 
        cipheredContent += ciphered + "\n"
    return cipheredContent

def writeFile(Pfilename:str, Pcontent:str):
    """Writes content into a specified file line by line"""
    file = open(Pfilename, "w", encoding="UTF-8")
    file.write(Pcontent)
    file.close()
    return None

def main ():
    print ("Program starting.")
    print ("\nCollecting plain text rows for ciphering.")
    words = collectWords()
    ciphered = cipherWords(words)
    print ("#### Ciphered text ####")
    print (ciphered)
    print ("#### Ciphered text ####")
    filename = input("Insert filename to save: ")
    if (len(filename) == 0):
        print ("File name not defined.\nAborting save operation.")
    else:
        writeFile(ciphered, filename)
        print ("Ciphered text saved!")
    print ("Program ending.")
    return None

main ()