print ("Program starting.")
print ("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")
length = len(name)
firstchar = name[0]
reversename = name[::-1]
print ("\nOptions:\n")
print ("1 - Print welcome message \n2 - Print the name backwards")
print ("3 - Print the first character\n4 - Show the amount of characters in the name \n0 - Exit")
choice = int(input("Your choice: "))
if choice == 1:
    print (f"Welcome {name}\n")
elif choice == 2:
    print (f"Your name backwards is \"{reversename}\"\n")
elif choice == 3:
    print (f"First character in name \"{name}\" is \"{firstchar}\"\n")
elif choice == 4:
    print (f"There are {length} characters in the name \"{name}\"\n")
elif choice == 0:
    print ("Exiting...")
else:
    print("Unknown choice")
print ("Program ending.")