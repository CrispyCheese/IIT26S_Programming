print ("Program starting.")

print ("\nCheck multiplicative persistence.")
number = input("Insert an integer: ")
counter = 0
if len(number) == 1:
    print (f"No more steps.\n\nThis program took {counter} step(s)\n")
else:
    while True:
        if len(number) == 1:
            print (f"No more steps.\n\nThis program took {counter} step(s)\n")
            break
        else:
            for i in range((len(number))):
                if (i == len(number) - 1):
                    result = result * int(number[i])
                    counter = counter + 1
                    print (f"{number[i]} = {result}")
                    number = str(result)
                    break
                elif (i == 0):
                    result = int(number[i])
                    print (f"{number[i]} * ", end="")
                else:
                    result = result * int(number[i])
                    print (f"{number[i]} * ", end="")  

print ("Program ending.")