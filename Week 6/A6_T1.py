def readAndPrint(Pfilename: str):
    file = open (Pfilename, 'r')
    while True:
        line = file.readline()
        if (len(line) == 0):
            break
        print (line, end="")
    return None

def main ():
    print ("Program starting.")
    print ("This program can read a file.")
    chosenFile = input("Input filename: ")
    print (f"### START \"{chosenFile}\" ###")
    readAndPrint(chosenFile)
    print (f"\n### END \"{chosenFile}\" ###")
    print ("Program ending.")
    return None

main ()