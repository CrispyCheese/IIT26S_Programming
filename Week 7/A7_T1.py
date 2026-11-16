def showIntegers(Pintegers:list):
    print (f"Displaying {len(Pintegers)} integers.")
    for i in range(0, len(Pintegers)):
        print (f"- Index {i} => Ordinal {i + 1} => Integer {Pintegers[i]}")
    return None

def collectIntegers()->list:
    integers = list()
    while True:
        feed = input("Insert positive integer(negative stops): ")
        if (feed.isnumeric() != True):      #If input is not numbers do nothing
            continue
        elif (int(feed) < 0):               #If input is empty stop loop
            break
        else:
            integers.append(int(feed))      #Add input into the list as integer
    return integers

def main():
    print ("Program starting.")
    print ("Collect positive integers.")
    posIntegers = collectIntegers()
    print ("Stopped collecting positive integers.")
    showIntegers(posIntegers)
    print("Program ending.")
    return None

main()