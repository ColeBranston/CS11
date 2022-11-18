# Name: Cole Braston
# Date: 2022/05/02
# Purpose: a financial calculator that gives an interactable menu for the user to interact with

# initializing the again variable in order to restart the program
again = "Y"

# main while loop containing program. Allows for restart
while again == "Y":

    # try statement that doesn't allow for erroring out
    try:
        # defining Yearly Pay so that it can be used later
        YearlyPay = 0

        # title of the program
        print("Salary Converter")
        print("----------------")

        # telling the user the purpose of the program
        print(
            "\nThis program converts a yearly salary to a daily, weekly,\nand monthly value."
        )

        # initializing my user-defined function
        def salary_converter(YearlyPay):

            # checking if the user's input is valid (above 1)
            while YearlyPay < 1:
                # telling the user to input a positive integer
                print("\nError, try a positive integer")
                # asking the user for their yearly pay
                YearlyPay = eval(input("\nWhat is your yearly salary?: "))

            # calculations for the monthly, weekly, and daily pay
            monthly = round(YearlyPay / 12, 2)
            weekly = round(YearlyPay / 52, 2)
            daily = round(YearlyPay / 365, 2)

            return monthly, weekly, daily

        # asking the user for their yearly pay
        YearlyPay = eval(input("\nWhat is your yearly salary?: "))

        #Calling the function
        monthly, weekly, daily = salary_converter(YearlyPay)

        # telling the user their yearly pay and their daily, weekly, and montly pays
        print(
            "\nYour Yearly salary is: $" + str(YearlyPay),
            "\nYour Monthly pay is: $" + str(monthly),
            "\nYour Weekly pay is: $" + str(weekly),
            "\nYour Daily pay is: $" + str(daily),
        )

        # asking the user if they want to restart the program
        again = input("Do you want to restart the program? (Y/N): ").upper()

    # except statement which doesn't allow the user to error out
    except:
        # telling the user that an error has occurred
        print("\nAn error has occured")
        # continueing the program from where it left off
        continue
