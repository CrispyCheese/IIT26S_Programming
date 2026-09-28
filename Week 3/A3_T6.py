print ("Program starting.")
print ("Welcome to unit converter program!\nFollow the menu instructions below\n")
print ("Options:\n1 - Length\n2 - Weight\n0 - Exit")
choice1 = int(input("Your choice: "))
if (choice1 == 0):
    print ("\nExiting...\n")
elif (choice1 == 1):
    print ("\nLength options\n1 - Meters to kilometers\n2 - Kilometers to meters\n0 - Exit")
    Lchoice = int(input("Your choice: "))
    if (Lchoice == 0):
        print ("Exiting...\n")
    elif (Lchoice == 1):
        Meters = float(input("Insert meters: "))
        print (f"{round(Meters,1)} m is {round(Meters / 1000,1)} km\n")
    elif (Lchoice == 2):
        Kmeters = float(input("Inser kilometers: "))
        print (f"{round(Kmeters,1)} km is {round(Kmeters * 1000,1)} m\n")
    else:
        print ("Unknown choice")
elif (choice1 == 2):
    print ("\nWeight options:\n1 - Grams to pounds\n2 - Pounds to grams\0 - Exit")
    Wchoice = int(input("Your choice: "))
    if (Wchoice == 0):
        print ("Exiting...")
    elif (Wchoice == 1):
        grams = float(input("Insert grams: "))
        print (f"{round(grams,1)} g is {round(grams * 0.0022,1)} lb")
    elif (Wchoice == 2):
        pounds = float(input("Insert pounds"))
        print (f"{round(pounds,1)} lb is {round(pounds * 453.592,1)} g\n")
    else:
        print ("Unknown choice\n")
else:
    print ("Unknown choice\n")
print ("Program ending.")