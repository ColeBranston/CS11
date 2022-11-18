#Name: Cole Branston
#Date: 2022/04/08
#Purpose: Print a list of characters using the chr() function

#initializing the again variable in order to restart the program
again = "Y"

#main while loop containing program
while again == "Y":
#try statement not allowing for erroring out
    try: 
        #printing the title of the program
        print("Character Display".rjust(10))
        print("------------------".rjust(10))

        #Telling the user the purpose of the program
        print("\nEach character in Python is represented by a number between 0 and 255. \nThe characters with values from 0-31 are non-printing characters and \ndon't display anything on the screen.")

        #asking the user for the higher and lower ranges in order to print out the characters
        lower = int(input("\nEnter the lower range: "))
        higher = int(input("Enter the higher range: "))

        #checking if the values inputted by the user were correct and actually had a character to output
        while lower <=32 or higher>=256  or higher <= lower:
            print("\nError, values incorrect, please restate values")
            lower = int(input("Enter the lower range: "))
            higher = int(input("Enter the higher range: "))

        #title of list of characters in user defined range
        print("\nValue Character".rjust(10))
        print("~~~~~~~~~~~~~~~~~".rjust(10))

        #for loop responsible for printing out the number and charater associated with it.
        #Defines x which is used for the print statement
        for x in range(lower, higher+1):
            print(x, chr(x))

        #asking the user if they want to restart the program
        again = input("\nWould you like to restart the program (Y/N): ").upper()

    #except statement not allowing for the user to error out
    except: 
        #Telling the user that there was an error in the values they inputted, asking them if they want to restart the program
        print("\nInvalid input, please try again")
        again = input("\nWould you like to restart the program (Y/N): ").upper()

