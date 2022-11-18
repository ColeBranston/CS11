# Name: Cole Branston
# Date: 2022/04/25
# Purpose: Allows the user to view the nth term in a fibonacci series of numbers

# initializng the again varibale in order to restart the program
again = "Y"

# main while loop which allows for the restart of the program
while again == "Y":

    # try statement that doesn't allow for errors
    try:
        # initializing the lists
        fibList = [0, 1]
        numendlist = []
        wordendinglist = []

        # title of program
        print("\nFibonacci Series")
        print("------------------")

        # telling the user the purpose of the program
        print(
            "The Fibonacci series is a sequence of numbers in which each number\nin the sequence equals the sum to the two preceding numbers.\nThe first two numbers in the sequence are 1.\nThe sequence of numbers are 1,1,2,3,5,8,13,21,..."
        )

        # appending fib numbers into list up to fib term 50
        while fibList.index(fibList[-1]) != 50:
            fib = fibList[-1] + fibList[-1 - 1]
            fibList.append(fib)

        # asking the user what term number they want to see
        fibIndexNum = str(
            input("\nWhich term would you like to see (up to the 50th): ")
        )

        for character in fibIndexNum:
            wordendinglist.append(int(character))

        # checking if the end of the number is a 1
        if wordendinglist[-1] == 1 and int(fibIndexNum) != 11:
            # setting the ending as st
            ending = "st"

        # checking if the number ends in a 2
        elif int(wordendinglist[-1]) == 2:
            # setting the ending as nd
            ending = "nd"

        # checking if the number ends in a 3
        elif int(wordendinglist[-1]) == 3:
            # setting the ending as rd
            ending = "rd"

        # checking if the number ends in anthing else
        else:
            # setting the ending as th
            ending = "th"

        # checking the user input is a valid input (above 0)
        if int(fibIndexNum) > 0:
            # printing the final statement telling the user the term and term number
            print(
                "\nThe", str(fibIndexNum) + ending, "term is", fibList[int(fibIndexNum)]
            )
        # if invalid input telling the user that their term was invalid
        else:
            print("\nEnter a positive value, please try again")

        # asking the user if they want to restart the program
        again = input("\nDo you want to restart the program? (Y/N): ").upper()

    # except statement that doesn't allow for erroring out
    except:
        # telling the user that an error has occured
        print("\nAn error has occured, please try again")
        # continuing the program where it left off
        continue
