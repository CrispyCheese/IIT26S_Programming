from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle, Polygon
import template

def getSqrParameters()->list:
    params = []
    print ("Insert square parameters")
    params.append(input("- Left edge position: "))
    params.append(input("- Top edge position: "))
    params.append(input("- Side length: "))
    params.append(input("- Fill color: "))
    params.append(input("- Stroke color: "))
    return params

def getCrclParameters()->list:
    params = []
    print ("Insert circle parameters")
    params.append(input("- Center X coord: "))
    params.append(input("- Center Y coord: "))
    params.append(input("- Radius: "))
    params.append(input("- Fill color: "))
    params.append(input("- Stroke color: "))
    return params

def drawSqr(Pdrawing:Drawing):
    squareParams = getSqrParameters()
    try:
        Pdrawing.add(Rect(insert=(int(squareParams[0]), int(squareParams[1])), size=(int(squareParams[2]), int(squareParams[2])), fill=squareParams[3], stroke=squareParams[4]))
    except ValueError:
        print ("Incorrect parameter inputs try again.")
    return None

def drawCircle(Pdrawing:Drawing):
    circleParams = getCrclParameters()
    try:
        Pdrawing.add(Circle(center=(int(circleParams[0]), int(circleParams[1])), r=int(circleParams[2]), fill=circleParams[3], stroke=circleParams[4]))
    except ValueError:
        print ("Incorrect parameter inputs try again.")
    return None

def saveConfirm()->str:
    while True:
        char = input("Proceed (y/n)?: ")
        if (char.lower() == "y" or char.lower() == "n"):
            break
        else:
            print ("Incorrect input")
    return char.lower()

def saveSvg(Pdrawing:Drawing):
    name = input("Insert filename: ")
    print (f"Saving file to\"{name}\"")
    while True:
        char = input("Proceed (y/n)?: ")
        if (char.lower() == "y"):
            Pdrawing.saveas(name)
            break
        elif (char.lower() == "n"):
            print ("Aborting save operation.")
            break
        else:
            print ("Incorrect input")
    return None

def main():
    drwng = Drawing()
    print ("Program starting.")
    while True:
        template.showOptions("Draw square,Draw circle,Save svg")
        userChoice = template.askChoice("Your choice", 3)
        if (userChoice == 0):
            print ("Exiting...\n")
            break
        elif (userChoice < 0 or userChoice > 3):
            print (f"Unknown choice \"{userChoice}\"!\n")
        elif (userChoice == 1):
            drawSqr(drwng)
            print ()
        elif (userChoice == 2):
            drawCircle(drwng)
            print()
        elif (userChoice == 3):
            saveSvg(drwng)
            print ("Vector saved successfully!\n")
    print ("Program ending.")

if __name__ == "__main__":
    main() 