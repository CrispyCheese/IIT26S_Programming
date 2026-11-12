def readFile(Pfilename:str) ->str:
    """Converts the files content into a list and filters out empty lines and returns the rest combined into a string"""
    file = open(Pfilename, "r", encoding="utf-8")
    lines = file.readlines()
    names = ""
    for i in range(0,len(lines)):
        if (len(lines[i].strip()) == 0):
            continue
        elif (len(names) > 0):
            names += ";" + lines[i].strip()
        else:
            names += lines[i].strip()
    return names

def analyseNames(Pnames:str):
    """String as input, splits it into a list, counts the words and characters and finds the length of longest and shortest words."""
    nameList = Pnames.split()
    shortest = len(nameList[0])
    longest = len(nameList[0])
    wordCount = len(nameList)
    characters = 0
    for i in range(0,wordCount):
        characters += len(nameList[i]) #Count the characters
        if (len(nameList[i]) < len(shortest)): #Checking if the indexed word is shorter than currently shortest one
            shortest = len(nameList[i]) #If true change to the longest one
        if (len(nameList[i] > longest)): #Checking if the indexed word is longer than currently longest one
            longest = len(nameList[i]) #If true change to the longest one
    print ("### REPORT BEGIN ###") #Printing out the results in the asked format.
    print (f"Name count - {wordCount}\nShortest name - {characters} chars")
    print (f"Longest name - {longest} chars\n Average name {(characters/wordCount):.2f} chars")
    print ("### REPORT END ###")
    return None


def main ():
    print ("Program starting.")
    print ("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ")
    print (f"Reading names from \"{filename}\".")
    names = readFile(filename)
    print ("Analysing names...")
    analyseNames(names)
    print ("Program ending.")

main ()