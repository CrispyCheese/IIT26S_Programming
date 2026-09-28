print ("Program starting.")
print ("Testing decision structures.")
number = int(input("Insert an integer: "))
print ("Options:\n1 - In one multi-branched decision\n2 - In multiple independent if statements\n0 - Exit")
choice = int(input("Your choice: "))
if (choice == 0):
    print ("Exiting...")
elif (choice == 1):
    if (number >= 400):
        number = number + 44
        print (f"Result is {number}")
    elif (number >= 200):
        number = number + 22
        print (f"Result is {number}")
    elif (number >= 100):
        number = number + 11
        print (f"Result is {number}")
    