print ("Program starting.\n")
compound = input("Insert a closed compound word: ")
length = len(compound)
lastchar = compound[length - 1]
reverse = compound[::-1]
print (f"The word you inserted is \'{compound}\' and in reverse it is \'{reverse}\'.")
print (f"The inserted word length is {length}")
print (f"The last character is \'{lastchar}\'\n")
print ("Take substring from the inserted word by inserting...")
Feed = input("1) Starting point: ")
start = int(Feed)
Feed = input("2) Ending point: ")
end = int(Feed)
Feed = input("3) Step size: ")
step = int(Feed)
substring = compound[start:end:step]
print (f"The word \'{compound}\' sliced to the defined substring is \'{substring}\'")
print ("Program ending.")