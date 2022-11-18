# Name: Cole Braston
# Date: 2022/05/02
# Purpose: Play rock, paper, scissors with the computer

#importing random for later use
import random

#defining the gameList used later on
gameList = ["", "Rock", "Paper", "Scissors"]

#defining the ai user defined function of the program
def ai():
    #choosing a random number between 1 and 3
    aiChoice = random.randint(1, 3)

    #returning the random choice
    return aiChoice

#initializing the again varibale in order to later restart the program
again = "Y"

#main while loop containing the program which allows for a restart
while again == "Y":

    #try statement not allowing for the user to error out
    try:

        #defining/redefining wins, losses, and ties used later on
        wins = 0
        losses = 0
        ties = 0

        #title of the program
        print("\nRock-Paper-Scissors")
        print("-------------------")

        #asking the user what their name is
        player = input("\nWhat is your name?: ")

        #checking if the game has ended yet
        while wins != 2 and losses != 2:

            #asking the user for their choice between rock, paper, and scissors
            choice = int(input("\n "+str(player)+" what is your choice (1-rock, 2-paper, 3-scissors): "))

            #Calling the function
            aiChoice = ai()

            #checking if I chose rock while the computer chose rock
            if choice == 1 and aiChoice == 1:

                #telling the user what you picked and what the computer picked
                print("\nYou picked", gameList[1], "and so did the computer. It is a tie")

                #increasing ties by 1
                ties+=1

            #checking if I chose rock while the computer chose paper
            elif choice == 1 and aiChoice == 2:

                #telling the user what you picked and what the computer picked
                print("\nYour", gameList[1], "got blocked by the computers", gameList[2])

                #increasing losses by 1
                losses+=1

            #checking if I chose rock while the computer chose scissors
            elif choice == 1 and aiChoice == 3:

                #telling the user what you picked and what the computer picked
                print("\nYour", gameList[1], "smashed through the computers", gameList[3])

                #increasing wins by 1
                wins+=1

            #checking if I chose paper while the computer chose rock
            elif choice == 2 and aiChoice == 1:

                #telling the user what you picked and what the computer picked
                print("\nYour", gameList[2], "blocked the computer's", gameList[1])

                #increasing wins by 1
                wins+=1

            #checking if I chose paper while the computer chose paper
            elif choice == 2 and aiChoice == 2:

                #telling the user what you picked and what the computer picked
                print("\nYou picked", gameList[2], "and so did the computer. It is a tie")

                #increasing ties by 1
                ties+=1

            #checking if I chose paper while the computer chose scissors
            elif choice == 2 and aiChoice == 3:

                #telling the user what you picked and what the computer picked
                print("\nYour", gameList[2], "got cut by the computer's", gameList[3])

                #increasing losses by 1
                losses+=1

            #checking if I chose scissors  while the computer chose rock
            elif choice == 3 and aiChoice == 1:

                #telling the user what you picked and what the computer picked
                print("\nYour", gameList[3], "got smashed by the computer's", gameList[1])

                #increasing losses by 1
                losses+=1

            #checking if I chose scissors while the computer chose paper
            elif choice == 3 and aiChoice == 2:

                #telling the user what you picked and what the computer picked
                print("\nYour", gameList[3], "cut through the computer's", gameList[2])

                #increasing wins by 1
                wins+=1

            #checking if I chose scissors while the computer chose scissors
            elif choice == 3 and aiChoice == 3:

                #telling the user what you picked and what the computer picked
                print("\nYou picked", gameList[3], "and so did the computer. It is a tie")

                #increasing ties by 1
                ties+=1


            #telling the user what the total wins, losses, and ties are 
            print("\n"+str(player), "Wins:", wins, "\nComputer Wins", losses, "\nties", ties)

        #checking if the player won
        if wins == 2:

            #Telling the player that they beat the computer
            print("\nCongratulations", player, "you beat the computer.")

        #checking if the computer 1 
        else:

            #telling the player that they lost
            print("\nUnfortunatley", player, "you didn't beat the computer, better luck next time.")

        #asking the user if they want to restart the program
        again = input("\nDo you want to restart the program? (Y/N): ").upper()

    #except statement now allowing the user to error out
    except:

        #telling the user that an error has occured
        print("\nAn error has occured, please try again")

        #continuing the program from where it left off
        continue