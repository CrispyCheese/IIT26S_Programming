def writeFile(Pcontent:list,Pfilename:str):
    file = open(Pfilename, 'w', encoding="utf-8")
    index = 0
    while (index != len(Pcontent)):
        file.write(Pcontent[index] + "\n")
        index += 1
    file.close()
    return None

def main ():
    print ("Program starting.")
    firstName = input("Insert first name: ")
    lastName = input("Insert last name: ")
    filename = input("Insert filename: ")
    content = firstName.strip() + ";" + lastName.strip()
    content = content.split(';')
    writeFile(content,filename)
    print ("Program ending.")
    return None

main ()