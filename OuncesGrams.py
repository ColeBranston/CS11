# Name: Cole Branston
# Date: 2022/04/06
# Purpose: This program converts ounces to grams.

#defining the again variable in order to restart the program
again = "Y"

#Main whole loop containg all the program 
while again == "Y":
    #try statement not allowing for errors within the code
    try:
        #title of the program
        print("Grams to Ounces Converter".rjust(10))
        print("--------------------------".rjust(10))

        print("This program converts ounces to grams in a table")

        #Asking the user for the higher and lower number for the table
        lower = int(input("\nEnter a lower number: "))
        higher = int(input("Enter the higher number: "))

        #printing the headers of the table
        print("Ounces".rjust(5), "Grams".rjust(10))
        print("--------".rjust(5), "---------".rjust(7))

        #conversions from ounces to grams in the table
        for ounces in range (lower, higher+1):
            grams = ounces* 28.35
            print(str(round(ounces,2)).rjust(5), str(round(grams,2)).rjust(10))


        #asking the user if they want to restart the program
        again = input("\nDo you want to restart the program (Y/N): ").upper()

    except:
        #telling the user that an error has occurred
        print("\nError, Try a whole number integer.")
         #asking the user if they want to restart the program
        again = input("\nDo you want to restart the program (Y/N): ").upper()
        