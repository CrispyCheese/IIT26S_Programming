print ("Program starting.")
print ("Insert two integers.")
num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer: "))
numbersum = int(num1 + num2)
print ("Comparing inserted integers.")
if (num1>num2):
    print ("First integer is larger")
elif (num2>num1):
    print ("Second integer is larger")
else:
    print ("Integers are the same")
print (f"\nAdding integers together\n{num1} + {num2} = {numbersum}\n")
print ("Checking parity of sum...")
if numbersum%2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")
print ("Program ending.")