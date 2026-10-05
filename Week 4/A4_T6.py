print ("Program starting.")

number = int(input("Insert a positive integer: "))
counter = 0
if (number > 1):
    print (number, end=" -> ")
while True:
    if (number == 2):
        counter = counter + 1
        print ("1")
        break
    elif (number % 2 == 0):
        number = int(number / 2)
        counter = counter + 1
        print (number, end=" -> ")
    else:
        number = int((number * 3) + 1)
        counter = counter + 1
        print (number, end=" -> ")
print (f"Sequence had {counter} total steps.\n")

print ("Program ending.")