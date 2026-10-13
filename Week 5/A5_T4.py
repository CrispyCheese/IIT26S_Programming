def askDimension(PPrompt: str) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Feed = PWidth * PHeight
   return Feed

def main():
   print ("Program starting.")
   PWidth = askDimension("width")
   PHeight = askDimension("height")
   Area = calcRectangleArea(PWidth, PHeight)
   print (f"\nArea is {round(Area, 1)}²")
   print ("Program ending.")

main()