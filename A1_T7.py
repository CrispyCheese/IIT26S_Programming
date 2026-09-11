print ("Calculate fuel consumption")
Feed = input ("Enter travel distance in kilometers:")
Distance = int(Feed)
Feed = input ("Enter fuel usage in liters:")
Fuel = int(Feed)
Consumption = Fuel / Distance * 100
Consumption = round (Consumption)
print (f"Fuel consumption is {Consumption} L per 100km")