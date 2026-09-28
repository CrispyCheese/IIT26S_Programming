print ("Program starting.")
print ("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")
print ("\nOptions: \n1 - Print welcome message \n0 - Exit")
choice = int(input("Your choice: "))
if choice == 0:
    print ("Exiting...\n")
elif choice == 1:
    print (f"Welcome {name}!\n")
else:
    print ("Unknown option\n")
print ("Program ending.")