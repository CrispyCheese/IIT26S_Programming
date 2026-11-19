import random
random.seed(1234)

def showOptions():
    print ("\nOptions:\n1 - Rock\n2 - Paper\n3 - Scissors\n0 - Quit game")
    return None

def getChoice()->int:
    """Asks user for the choice and verifies it is an valid input"""
    choice = int()
    while True:
        feed = input("Your choice: ")
        if (feed.isnumeric()):              #Checking if non numbers in the input
            if (0 <= int(feed) <= 3):       #Check if the input is one of the options
                choice = int(feed)          #Save input in choice
                break                       #End the loop
            else:
                print ("Please input a valid number") 
        else: print ("Please input a number from 0 to 3")
    return choice

def showHand(Pplayer:str, Phand:int):
    """Prints the info about players chosen hand and the corresponding Ascii art"""
    if (Phand == 1):
        print (f"{Pplayer} chose rock.\n")
        print ("    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)\n")
    elif (Phand == 2):
        print (f"{Pplayer} chose paper.\n")
        print ("     _______\n---'    ____)____\n           ______)\n          _______)\n         _______)\n---.__________)\n")
    elif (Phand == 3):
        print (f"{Pplayer} chose scissors.\n")
        print ("    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)\n")
    return None

def handString(Pchoice:int):
    """Returns a string of the players hand choice"""
    if (Pchoice == 1):
        return "rock"
    elif (Pchoice == 2):
        return "paper"
    else:
        return "scissors"

def whoWon(Pplayer:int, Pbot:int)-> int:
    """Checks who won the round"""
    result = int()
    if (Pplayer == Pbot):       #It's a draw if the choices are same
        result = 2
    elif (Pplayer == 1):        #Checking if player won or lost with rock
        if (Pbot == 2):         
            result = 0          
        else:
            result = 1          
    elif (Pplayer == 2):        #Checking if player won or lost with paper
        if (Pbot == 1):
            result = 1          
        else:
            result = 0          
    elif (Pplayer == 3):        #Checking if player won or lost with scissors
        if (Pbot == 1):
            result = 0          
        else:
            result = 1          
    return result

def playRPS(Puser:str, Pchoice:int, PplayerStats:list[int], PbotStats:list[int]):
    """Plays a round of rock paper scissors and updates the stats depending on who won"""
    botsChoice = random.randint(1, 3)           #Get a random hand for the bot
    print ("#" * 25)
    showHand(Puser, Pchoice)                    #Print users hand choice and ascii art
    print ("#" * 25)
    showHand("RPS-3PO", botsChoice)             #Print bots hand choice and ascii art
    print ("#" * 25)
    result = whoWon(Pchoice, botsChoice)        #Get results of the round
    if (result == 0):                           #Player lost
        PplayerStats[1] += 1                
        PbotStats[0] += 1
        print (f"\nRPS-3PO {handString(botsChoice)} beat {Puser} {handString(Pchoice)}")
    elif (result == 1):                         #Player won
        PplayerStats[0] += 1
        PbotStats[1] += 1
        print (f"\n{Puser} {handString(Pchoice)} beat RPS-3PO {handString(botsChoice)}")
    elif (result == 2):                         #Draw
        PplayerStats[2] += 1
        PbotStats[2] += 1
        print (f"\nDraw! Both players chose {handString(Pchoice)}")
    return None

def showResults(Pname:str, Pplayer:list[int], Pbot:list[int]):
    """Prints out results from the stats lists"""
    print ("\nResults:")
    print (f"{Pname} - wins ({Pplayer[0]}), losses ({Pplayer[1]}), draws ({Pplayer[2]})")
    print (f"RPS-3PO - wins ({Pbot[0]}), losses ({Pbot[1]}), draws ({Pbot[2]})\n")
    return None

def main():
    print ("Program starting")
    playerStats:list[int] = [0, 0, 0]           #List to contain players wins, losses and draws
    botStats:list[int] = [0, 0, 0]              #List to contain bots wins, losses and draws
    print ("Welcome to the rock-paper-scissors game!")
    player = input("Insert player name: ")
    print (f"\nWelcome {player}!\nYour opponent is RPS-3PO.")
    print ("Game starts...")
    while True:                                 #Play rock paper scissors against the bot until user decides to stop
        showOptions()
        playersChoice = getChoice()             
        if (playersChoice == 0):                                            #Exit chosen
            if (playerStats.count(0) == 3 and botStats.count(0) == 3):      #If no hands were played
                print ("No games played")
                break
            else:
                showResults(player, playerStats, botStats)                  #Show the results of the rounds played
                break
        else:
            print ("Rock! Paper! Scissors! Shoot!\n")                       
            playRPS(player, playersChoice, playerStats, botStats)           #Play rock paper scissors
    playerStats.clear()
    botStats.clear()
    print ("Program ending.")
    return None

if __name__ == "__main__":
    main() 