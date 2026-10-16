def main():
    print ("Program starting.\n")
    word = input("Insert word: ")
    frameWord(word)
    print ("Program ending.")
    return None

def frameWord(PWord):
    frame = "*" * (len(PWord) + 4)
    print (f"\n{frame}\n* {PWord} *\n{frame}\n")
    return None

main()