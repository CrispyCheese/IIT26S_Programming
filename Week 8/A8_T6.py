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
    squareParameters = getSqrParameters()

def drawCircle(Pdrawing:Drawing):
    circleParameters = getCrclParameters()

def saveSvg(Pdrawing:Drawing):
    filename = input("Insert filename: ")
    print (f"Saving file to\"{filename}\"")
    saveConfirm = input("Proceed (y/n)?: ")
    if (saveConfirm.strip().lower() == "y"):
        file = open(filename, "w", encoding="")
        file.write(Pdrawing)
    return None



def main():
    drwng = Drawing()
    print ("Program starting.")
    while True:
        template.showOptions("Draw square, Draw circle, Save svg")
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
    print ("Program ending.")

if __name__ == "__main__":
    main() 