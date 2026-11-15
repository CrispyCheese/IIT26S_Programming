def remvEmpty(Plist:list)-> str:
    """List as input filters out empty returning rest in a string"""
    cleaned = ""
    for i in range(0,len(Plist)):           #Loop through the list to filter out empty lines.
        if (len(str(Plist[i]).strip()) == 0): 
            continue
        else:
            cleaned += str(Plist[i]).strip() + ";"
    return cleaned

def readFile(Pfilename:str) ->list:
    file = open(Pfilename, "r", encoding="UTF-8")
    lines = file.readlines()            #Reads all the lines in the file and saves them as a list
    file.close()
    return lines

def analyseNames(Pnames:str):
    """String as input, counts the words and characters and finds the of longest and shortest words."""
    shortest = len(Pnames)              #Initialise the shortest word length as the length of input string.
    wordCount = 0
    longest = 0
    length = 0                          #Current words length.
    characters = 0                      #Total characters in the input string.
    for i in range(0,len(Pnames)):
        if (Pnames[i].isalpha()):       #Check that the indexed part of string is a character.
            length += 1
        elif (Pnames[i] == ";"):        #";" marks the end of the words in the input string.
            characters += length
            wordCount += 1
            if (length < shortest):     #Compare the shortest to the current words length and replace with current if true.
                shortest = length
            if (length > longest):      #Compare the longest to the current words length and replace with current if true.
                longest = length        
            length = 0                  #Reset the current words length to zero
    average = (characters / wordCount)
    return (f"Name count - {wordCount}\nShortest name - {shortest} chars\nLongest name - {longest} chars\nAverage name - {average:.2f} chars")

def main ():
    print ("Program starting.")
    print ("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ")
    print (f"Reading names from \"{filename}\".")
    names = readFile(filename)
    namesClean = remvEmpty(names)
    print ("Analysing names...")
    result = analyseNames(namesClean)
    print ("### REPORT BEGIN ###")          
    print (result)                  #Printing out the results in the asked format.
    print ("### REPORT END ###")
    print ("Program ending.")
    return None

main ()