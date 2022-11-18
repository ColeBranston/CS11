#Cole Branston
#Date: 12/14/2020
#Purpose: This program runs a game called poison penny, a two player strategy game. There are 12 pennies and 1 nickel. Who ever gets the nickel loses. Out of the two players each person gets a turn, they get to decide how many pennies they take. The players can either take 1 or 2 pennies.

#Telling the user what the program does
print("This program runs a game called poison penny, a two player strategy game. There are 12 pennies and 1 nickel. Who ever gets the nickel loses. Out of the two players each person gets a turn, they get to decide how many pennies they take. The players can either take 1 or 2 pennies.")
#defining turn so that the players can swtich
#Allowing for the user to play the game agai
again = "Y"
while again == "Y":
    #try statment not allowing for erroring out
    try:
        #Asking the user(s) for their names
        player1 = input("\nEnter Player1's name: ")
        player2 = input("\nEnter Player2's name: ")
        #defining total and using to determine whether the code should run or not
        total = 12
        turn = 1
        while total > 0:
            if turn == 1:
                player = player1
            else:
                player = player2
            #Telling the user(s) who's turn it is and asking the amount of pennies the user wants to take
            print(player,"'s","turn")
            print("\n---------------")
            Pennies_Taken = int(input("How many pennies do you want to take 1 or 2?: "))
            #Asking the user to re-enter an amount if value is greater than the total
            while Pennies_Taken>total:
                Pennies_Taken =  int(input("How many pennies do you want to take 1 or 2?: "))
            #Asking the user to re-enter the amount of pennies they want to take if they give a value greater than 2
            while Pennies_Taken >=3:
                print("\nTry 1 or 2")
                Pennies_Taken = int(input("How many pennies do you want to take 1 or 2?: "))

            #Telling the users the amount of pennies that are left after the other players taking pennies turn
            if Pennies_Taken ==1:
                total -=1
                print("\nThere is", total, "Pennies left")
            elif Pennies_Taken ==2:
                total -=2
                print("\nThere is", total, "Pennies left")

            #Switching turns 
            if player ==player1:
                turn= 2
            else:
                turn = 1
       
        if player != player1:
            print(player1, "you lose")
            print(player2, "you win")
        else:
            print(player2, "you lose")
            print(player1, "you win")

        #Asking the user if they want to play again
        again = input("\nWould you like to play again? (Y/N): ").upper()
        #If they say no say thankyou for playing
        if again =="N":
            print("\nThankyou for playing, come back soon")

    #not allowing for erroring out
    except:
        print("\nerror, try program again")
        again = input("\nWould you like to play again? (Y/N): ").upper()
        