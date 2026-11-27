import mathLib
import template

def askValue(Pprompt:str)->float:
    try:
        number = float(input(f"{Pprompt}: "))
    except ValueError:
        print ("Please insert a number")
    return number

def main()->None:
    print ("Program starting.")
    value1 = 0
    value2 = 0
    while True:
        template.showOptions("Add,Subtract,Multiply,Divide")
        calcChoice = template.askChoice("Your choice", 4)
        if (calcChoice == 0):
            print ("Exiting program\n")
            break
        elif (0 >= calcChoice or  calcChoice >= 4):
            print (f"Unknown choice \"{calcChoice}\"!")
        elif (calcChoice == 1):
            value1 = askValue("Insert first to be summed value")
            value2 = askValue("Insert second to be summed value")
            result =mathLib.add(value1, value2)
            print (f"{value1} + {value2} = {result:.8f}")
        elif (calcChoice == 2):
            value1 = askValue("Insert value to be subtracted from")
            value2 = askValue("Insert value to subtract")
            result =mathLib.subtract(value1, value2)
            print (f"{value1} - {value2} = {result:.8f}")
        elif (calcChoice == 3):
            value1 = askValue("Insert value to be multiplied")
            value2 = askValue("Insert value for multiplier")
            result =mathLib.multiply(value1, value2)
            print (f"{value1} * {value2} = {result:.8f}")
        elif (calcChoice == 4):
            value1 = askValue("Insert value to be divided")
            value2 = askValue("Insert value of the divider")
            result =mathLib.divide(value1, value2)
            print (f"{value1} / {value2} = {result:.8f}")
    print ("Program ending.")
    return None

if __name__ == "__main__":
    main() 