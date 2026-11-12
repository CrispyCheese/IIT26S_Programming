#Reads the named file adds the content of lines into a list and returns that list
def readFile(Pfilename:str)-> list:
    content = list()
    index = 0
    file = open(Pfilename, "r", encoding="utf-8")
    while True:
        line = file.readline()
        if (len(line) == 0):
            break
        content.append(line)
        index += 1
    file.close()
    return content

#Writes the input lists conatent line by line into the target file.
def writeFile(Pcontent:list,Pfilename:str):
    file = open(Pfilename, "w", encoding="utf-8")
    for i in range(0,len(Pcontent)):
        file.write(Pcontent[i])
    file.close()
    return None
    
def main ():
    print ("Program starting.")
    print ("This program can copy a file")
    source = input("Insert source filename: ")
    destination = input("Insert destination filename: ")
    print (f"Reading file '{source}' content.")
    content = readFile(source)
    print ("File content ready in memory.")
    print (f"Writing content into file '{destination}'.")
    writeFile(content,destination)
    print ("Copying operation complete.")
    print ("Program ending.")
    return None

main ()