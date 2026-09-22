print ("Program starting.")
Feed = input("Insert fahrenheits: ")
fahrenheit = float(Feed)
celsius = (fahrenheit - 32) / 1.8
print (f"{fahrenheit}°F is {round(celsius, 1)}°C")
print ("Program ending.")