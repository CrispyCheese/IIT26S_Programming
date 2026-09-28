print ("Program starting.")
print ("Testing decision structures.")
number = int(input("Insert an integer: "))
print ("Options:\n1 - In one multi-branched decision\n2 - In multiple independent if statements\n0 - Exit")
choice = int(input("Your choice: "))
if (choice == 0):
    print ("Exiting...\n")
elif (choice == 1):
    if (number >= 400):
        number = number + 44
    elif (number >= 200):
        number = number + 22
    elif (number >= 100):
        number = number + 11
    print (f"Using one multi-branched decision structure.\nResult is {number}\n")
elif (choice == 2):
    if (number >= 400):
        number = number + 44
    if (number >= 200):
        number = number + 22
    if (number >= 100):
        number = number + 11
    print (f"Using multiple independent if-statements structure.\nResult is {number}\n")
else:
    print ("Unknown option")
print ("Program ending.")