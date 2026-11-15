def writeFile(Pcontent:str,Pfilename:str):
    file = open(Pfilename, 'w', encoding="UTF-8")
    file.write(Pcontent)    
    file.close()
    return None

def main ():
    print ("Program starting.")
    firstName = input("Insert first name: ")
    lastName = input("Insert last name: ")
    filename = input("Insert filename: ")
    content = firstName.strip() + "\n" + lastName.strip() + "\n"
    writeFile(content,filename)
    print ("Program ending.")
    return None

main ()