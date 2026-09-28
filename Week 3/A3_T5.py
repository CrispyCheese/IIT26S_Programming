print ("Program starting \n")
print ("Options:")
print ("1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n3 - Exit")
choice = int(input("Your choice: "))
if (choice == 0):
    print ("Exiting...\n")
elif (choice == 1):
    Celsius = float(input("Insert the amount of Celsius: "))
    print (f"{Celsius} °C equals to {round((Celsius * 1.8) + 32,1)} °F\n")
elif (choice == 2):
    Fahrenheit = float(input("Insert the amount of Fahrenheit"))
    print (f"{Fahrenheit} °F equals to {round((Fahrenheit - 32) / 1.8,1)} °C\n")
else:
    print("Unknown choice\n")
print("Program ending.")