DELIMITER = ","
def collectWords() -> str:
    words = str()
    while True:
        feed = input("Insert word(empty stops): ")
        if (len(feed) == 0):
            break
        elif (len(words) > 0):
            words += DELIMITER + feed
        else:
            words = feed
    return words

def analyzeWords(PWord: str):
    wordList = PWord.split(DELIMITER)
    wordCount = len(wordList)
    characters = 0
    for i in range(wordCount):
        feed = wordList[i]
        characters += len(feed)
    Avg = characters / wordCount
    print (f"- {wordCount} words\n- {characters} Characters")
    print ("- {:.2f} Average word length".format(Avg)) 
        
def main():
    print ("Program starting.")
    words = collectWords()
    analyzeWords(words)
    print ("Program ending.")

main()