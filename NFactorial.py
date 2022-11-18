# Name: Cole Branston
# Date: 2022/04/13
# Purpose: ask the user for a number and use for loops to print it out as a factorial

#defining again to allow for the while loop to start and restart
again = "Y"

#main while loop with all of program inside. Allows for the restart of program
while again == "Y":
    #try statement that doesn't allow erroring out
    try: 
        #title of program
        print("N Factorial Calculator".rjust(10))
        print("----------------------".rjust(10))

        #telling the user what the purpose of this program is
        print("\nThis program will calculate the N Factorial for any given positive integer".rjust(10))
        factorialnum = int(input("\nEnter a positive integer: "))

         #while user inputted value in invalid ask the user again and tell them to use a positive integer
        while factorialnum <=0:
            print("\nuse a positive integer")
            factorialnum = int(input("\nEnter a positive integer: "))
            
        #checking if the number inputted by the user is valid and continuing program
        if factorialnum >= 1:
            #first part of equation, also printing it out for the user to see
            print("\n",str(factorialnum)+"!", "= ", end ="")

            #main second part of equation, also printing it out for the user to see
            total = factorialnum
            for x in range(1, factorialnum):
                total *= x
                print(x, "x ", end = "")

            #final part of equation that prints final digit and outputs the NFactorial
            print(factorialnum, "=", total)

        #asking the user if they want to restart the program
        again = input("\nDo you want to restart the program (Y/N): ").upper()

    #except statement not allowing for erroring out
    except:
        #telling the user than an error has occured and asking the user if they want to restart the program
        print("\nAn error has occured, please try again")
        again = input("\nDo you want to restart the program (Y/N): ").upper()
