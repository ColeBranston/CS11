# Name: Cole Braston
# Date: 2022/05/02
# Purpose: Program that plays over under game

#importing random for later use
import random

#defining a user defined function that simulates the rolling of 2 dice and returns those values along with their sum
def randomDice():
    #randomly choosing a number between 1 and 6 for Dice 1
    dice1 = random.randint(1,6)

    #randomly chooseing a number between 1 and 6 for Dice 2
    dice2 = random.randint(1,6)

    #calculating the sum of the two randomly "rolled" numbers
    sum = dice1 + dice2

    #returning the sum, dice1, and dice2 values for later use
    return sum, dice1, dice2

#initializng again for the restart of the program
again = "Y"

while again == "Y":
    #defining total for score, reroll for reroll of the dice, again to restart the program, and write to write in a text document
    total = 500
    reroll = "Y"

    #try statement not allowing for the user to error out
    try:
        #title of the program
        print("Over / Under Game of Chance")
        print("---------------------------")

        #telling the user the purpose of the program and how to play the game
        print("\nOver / Under is a game of chance played with two six-sided dice.\nThe dice are rolled and the sum of their faces is calculated.\nThe game player bets on whether or not the sum is over 7, under 7,\nor exactly even to 7. Their bet is matched if they guess correctly on\nover or under and their bet is doubled if they guess correctly that\nthe sum is even to 7.")

        #opening the highscore document in order to read highscores
        highscores = open("highscore.txt", "r")

        #Reading the first line of the highscores document
        line = highscores.readline()

        #checking if the line is not blank and itterating through the following code
        while line != "":

            #splitting the lines contents into a list called highscorelist
            highscorelist = line.split("-")

            #assigning variables to the different elements of the list
            highscoreName = highscorelist[0]
            highscoreNum = highscorelist[-1]
            
            #telling the user the current highscore and who it belongs to
            print("\nThe current highscore is $"+highscoreNum, "by", highscoreName)
            
            #reading the next line of the document
            line = highscores.readline()
        
        #closing the highscores document
        highscores.close()

        #Telling the user the amount of money they have/start off with
        print("\nYou have $"+str(total))

        #checking if reroll is equal to yes and itterating through the following
        while reroll == "Y":

            #asking the user for the amount of money they want to bet 
            bet = eval(input("\nEnter your bet: (1 - $"+str(total)+"): "))

            #checking that the user is betting an amount of money that they have
            while bet > total:

                #telling the user that they don't have enough money to bet their amount
                print("\nYou do not have enough funds, please use only the money you have")

                #asking the user what they want to bet
                bet = eval(input("\nEnter your bet: (1 - $"+str(total)+"): "))

            #asking the user for what their guess is
            guess = input("Enter your guess (O/U/E): ").upper()

            #Calling function
            sum, dice1, dice2 = randomDice()

            #telling the user what the computer rolled
            print("\nThe computer rolled a", dice1,"and", dice2,"for a total of", sum)

            #checking if the user said Over and that the sum is greater than 7
            if guess == "O" and sum > 7:
                #adding the bet to the user's total score/money
                total+=bet

                #telling the user that they won
                print("\nCongrats! you win")

            #Checking if the user said Under and if the sum is less than 7
            elif guess == "U" and sum < 7:

                #adding the user's bet to their total score/money
                total+=bet

                #telling the user that they won
                print("\nCongrats! you win")

            #checking if the user said equal and the sum is equal to 7
            elif guess == "E" and sum == 7:

                #adding double the user's bet amount to the total score/money
                total += bet*2
                
                #telling the user that they won
                print("\nCongrats! you win")

            #checking for anything else
            else:

                #subtracting the user's bet from their total score/money
                total-=bet

                #telling the user that they lost
                print("\nUnfortunately you lost")

            #telling the user their new total score/money
            print("\nYou have $", str(total))

            #checking if the user's total = 0
            if total == 0:

                #telling the user that they lost the game
                print("\nGame Over, please play again")

                #breaking the loop
                break

            #if anything else than itterating through the following
            else:
                #asking the user if they want to reroll
                reroll = input("\nDo you want to roll the dice again? (Y/N): ").upper()

        #asking the user if they want to restart the program
        again = input("\nDo you want to restart the program? (Y/N): ").upper()

        #checking if the user said no
        while again == "N":
            #opening the highscores document
            highscores = open("highscore.txt", "r")

            #reading the first line of the document
            line = highscores.readline()

            #checking the line is not blank
            while line != "":

                #splitting the line into a list
                highscorelist = line.split("-")

                #reading the elements of the list
                highscoreName = highscorelist[0]
                highscoreNum = highscorelist[-1]
                
                #checking if the user's score was better than the highscore
                if total > int(highscoreNum):

                    #telling the user htat they beat the highscore
                    print("\nCongratulations, your score of", total, "just beat the highscore of", highscoreNum, "by", highscoreName)

                    #asking the user for their name
                    newname = input("\nWhat is your name: ")

                    #telling the user that their score became the new highscore
                    print("\nCongratulations", newname, "you now have the highscore.")

                    #breaking the program
                    break

            #closing the highscores document
            highscores.close()

            #checking if the user's score was greater than the highscore
            if total > int(highscoreNum):

                #opening the highscores document in order to write in it
                highscores = open("highscore.txt", 'w')
                
                #writing the name of the current user and their score into the highscores document
                highscores.write(newname+"-"+str(total))
        
            #closing the highscores document
            highscores.close()

    #except statement not allowing for erroring out
    except:

        #telling the user that an error has occured
        print("\nAn error has occurred")

        #continuing the program from where it left off
        continue