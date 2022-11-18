#Name: Cole Branston 
#Date: 2022/05/15
#Purpose: create a program that simulates picking 5 random cards from a deck of cards

#importing random for later use
import random

#defining function 
def cards():

    #setting count to 0
    count = 0

    #Checking if count doesn't equal 5
    while count != 5:

        #increasing the count by 1
        count +=1

        #choosing a random suit from the list
        suit = random.choice(suitsList)
        number = random.choice(numbersList)
       
        #checking if the card had been drawn already
        while (str(suit)+str(number)) in cardsUsed:
            
            #rechoosing the suit from the list
            suit = random.choice(suitsList)

            #rechoosing the number from the list
            number = random.choice(numbersList)
        
        #adding the use card to the cardsUsed list in a set format
        cardsUsed.append(str(suit)+str(number))

        #telling the user their card
        print("\t", number, "of", suit)
           
       
#defining the numbers list
numbersList = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

#defining the suits list
suitsList = ["Spades", "Clubs", "Diamonds", "Hearts"]

#creating the cardsUse list
cardsUsed = []

#defining the again varible in order for a later restart
again = "Y"

#main while loop allowing the program to repeat
while again == "Y":

    #try statement not allowing the user to error out
    try:
   
        #calling the user-defined function, "cards"
        cards()
    
        #clearing the cardsUsed list so that cards can redrawn if asked
        cardsUsed.clear()
        
        #asking the user if they wish to restart the program
        again = input("\nDo you want to go again (Y/N): ").upper()

    #except statement now allowing for the user to error out
    except:

        #telling the user that an error has occured
        print("\nError, a problem has occured")

        #continuing the program from where the user left off
        continue