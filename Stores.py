# Name: Cole Branston
# Date: 2022/04/22
# Purpose: gets the total amount of money a user spent at multiple stores

#initializing the varible again to allow for the restart of the program
again = "Y"

#main while lopp containtaing program
while again == "Y":
    #defining variables such as total and numofsotres to be used in program
    total = 0
    numofstores = 0
    store = "Y"
    #checking if the user went to another store
    while store == "Y":
            #try statement not allowing for a user to error out
        try:
            #asking the user how much money they spent at this store
            spent = eval(input("How much did you spend at this store: "))
            #checking if spent not a positive integer
            while spent <0:
                #telling the user to enter a positive value
                print("\nEnter a positive Value")
                #asking the user how much money they spent
                spent = eval(input("\nHow much did you spend at this store: "))
            #adding the amount spent to the total
            total+=spent
            #asking the user if they went to another store
            store = input("Did you go to any other store (Y/N): ").upper()     

            #if the user went to another store than increase the numofstores by 1
            numofstores+=1
            
            #checking if they went to any other stores and if no than doing the following
            if store == "N":
                #telling the user the amount of stores that they went to and telling the user the total that they spent
                print("\nYou went to", numofstores, "stores and spent a total of $"+str(total))
                break

        #except statment not allowing for the user to error out
        except:
            #telling the user that an error has occurred
            print("\nAn error has occurred, try again")

    #asking the user if they want to restart the program
    again = input("\nDo you want to restart the program (Y/N): ").upper()
    