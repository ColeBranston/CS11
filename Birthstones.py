# Name: Cole Branston
# Date: 2022/04/25
# Purpose: This program will pick a gift based off a month entered 

#iniitlaizing the again varibale in order to allow for the program to restart
again = "Y"

#main while loop containing code. While checks if again == "Y" in order to start/restart the loop
while again == "Y":

    #try statement which doesn't allow for the user to error out
    try:

        #main lists containing str data 
        monthlist = ["","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        modernlist = ["","Garnet", "Amethyst", "Aquamarine", "Diamond", "Emerald", "Pearl, Moonstone", "Ruby", "Peridot", "Sapphire", "Opal, Tourmaline", "Yellow Topaz, Citrine", "Blue Topaz, Turquoise"]
        traditionallist = ["","Garnet", "Amethyst", "Bloodstone", "Diamond", "Emerald", "Alexandrite", "Ruby", "Sardonyx", "Sapphire", "Tourmaline", "Citrine", "Zircon, Turquoise, Lapis Lazuli"]

        #telling the user the title of the program
        print("Birthstones")
        print("-----------")

        #describing the purpose of the program to the user
        print("\nJewelry stores often sell birthday presents based on a person's birthstone.\n When a store clerk enters the number of the month, the correct birthstone is \nprinted.")

        #asking the user of what month they wish to find there birthstones for
        month =int(input("\nEnter a month number (1-12): "))

        #checking if the users input is between the range given
        if month > 0 and month < 13:
            #checking if the list information is the same
            if modernlist[month] == traditionallist[month]:
                #changng the statement to a more efficient statement (only telling them one string for both) and informing the user of their birth stone and birth month
                print("\nYour modern birthstone and traditional birthstone for", monthlist[month], "is", modernlist[month])
            #if the list data is not the same than printing the full sentence that tells the user the modern birthstone, traditional birthstone, and month that they were born
            else:
                print("\nYour modern birthstone for", monthlist[month], "is", modernlist[month], "and your traditional birthstone is", traditionallist[month])
        #checking if the num imputted by the user is not imbetween the range given
        else:
            #telling the user that an error has occured and asking them to restart
            print("\nError, try again. Use a number within range")

        #asking the user if they want to restart the program
        again = input("\nDo you want to restart the program? (Y/N): ").upper()
    #except statement not allowing for the user to error out
    except:
        #telling the user that an error has occured 
        print("\nAn error has occured, please try again")
        #continuing the program as if the error didn't happen
        continue

