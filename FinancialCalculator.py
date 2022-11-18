# Name: Cole Braston
# Date: 2022/05/02
# Purpose: Uses a user-defined function that converts a persons yearly salary into daily, weekly, and monthly salaries

#menu list containing menu options
menulist = ["Calculate Simple Interest", "Calculate Compound Interest","Calculate Discounts", "Calculate Taxes", "Exit Program"]

#restart that stops whole while loop
restart = "Y"

#defining the simpleinterest() user defined function
def simpleinterest(principal, percentage, numyears):

    #telling the user the total interest that their investment made
    print("\nThe interest earned is $"+str(round(interest,2)))
    
    #telling the user the total profit they have made from their investments
    print("The total amount of your investment is $"+str(round(total,2)))

#defining the compoundinterest() user defined function
def compoundinterest(principal, percentage, numyears):

    #calculating the total profit that has been made by this investment
    total = (principal * ((1+(percentage/100)))**numyears)

    #calculating the interest earned from the user's investment
    interest = total - principal

    #telling the user their total interest earned
    print("\nThe compound interest earned is $"+str(round(interest,2)))
    
    #telling the user their total profit
    print("The total amount of your investment is $"+str(round(total,2)))

#defining the discounts() user defined function
def discounts(costofitem, perdiscount):

    #calciulating the amount of money the user saves with the discount
    discount = costofitem*(perdiscount/100)

    #calculating the total cost of the item
    discounteditem = costofitem - discount

    #telling the user the amount of money they saved
    print("\nThe discount is: $" + str(round(discount,2)))

    #telling the user the total cost of their item
    print("Your discounted price is: $"+str(round(discounteditem,2)))

#defining the taxes() user defined function
def taxes(amount, taxrate):

    #calculating the tax that the user has to pay
    tax = amount * (taxrate/100)

    #calculating the total amount of money that the user has to pay
    total = tax+amount
    
    #telling the user the amount of taxes paid for their item
    print("\nYour taxes on this purchase are $"+str(round(tax,2)))

    #telling the user the total bill
    print("Your total bill is $"+str(round(total,2)))
    
while restart == "Y": 

    try:

        principal = 0
        percentage = 0
        numyears = 0
        costofitem = 0
        perdiscount = 0
        amount = 0
        taxrate = 0

        #title of program
        print("\nFinancial Calculator")
        print("--------------------")

        print("\nMake your choice from the menu below.")

        #printing the menu for the user to interact with
        print("\n1.", menulist[0],"\n2.", menulist[1],"\n3.", menulist[2],"\n4.", menulist[3],"\n5.", menulist[4])

        #allowing the user to choose which program they want to run
        choice = int(input("\n>>>"))

        #checking if the user's input is invalid, 
        while choice >5 or choice <1:
            #telling the user that an error has occurred
            print("\nInvalid Input, try again")

            print("\nMake your choice from the menu below.")

            #reprinting the menu for the user to interact with
            print("\n1.", menulist[0],"\n2.", menulist[1],"\n3.", menulist[2],"\n4.", menulist[3],"\n5.", menulist[4])

            #allowing the user to interact with the menu and choose which program they wish to run
            choice = int(input("\n>>>"))

        #checking if they chose program 1
        while choice == 1:

            #title of program
            print("\nSimple Interest Calculator")
            print("--------------------------")

            #asking the user for their initial value (principal)
            principal = eval(input("\nEnter the amount of the principal: $"))

            #asking the user the percentage yearly rate of interest
            percentage = eval(input("\nEnter the yearly rate of interest as a percentage: "))

            #asking the user for the num of years for their investment
            numyears = int(input("\nEnter the number of years: "))

            #calculating the interest gained from their investment
            interest = (principal * (percentage/100))*numyears

            #calculating the user's total profit
            total = principal + interest

            #itterating through the user defined function
            simpleinterest(principal, percentage, numyears)

            #resetting choice so that the program doesn't restart
            choice = 0

        #checking if the choice was program 2
        while choice == 2:

            #title of program
            print("\nCompound Interest Caclculator")
            print("---------------------------")

            #asking the user for the initial amount of money (principal)
            principal = eval(input("\nEnter the amount of the principal: $"))

            #asking the user for the percentage rate of interest they expect to earn
            percentage = eval(input("\nEnter the yearly rate of interest as a percentage: %"))

            #asking the user for the num of years for their investment
            numyears = int(input("\nEnter the number of years: "))

            #itterating through the user defined function
            compoundinterest(principal, percentage, numyears)

            #resetting choice so that the program doesn't restart
            choice = 0

        while choice == 3:

            #title of program
            print("\nDiscount Calculator")
            print("-------------------")

            #asking the user for the cost of their item
            costofitem = eval(input("\nEnter the amount of your item: $"))

            #asking the user for the percentage discount rate of their item
            perdiscount = eval(input("Enter the discount rate as a percentage: %"))

            #itterating through the user defined function
            discounts(costofitem, perdiscount)

            #resetting choice so that the program doesn't restart
            choice = 0

        while choice == 4:
            #title of program
            print("\nTax Calculator")
            print("--------------")

            #asking the user the total amount that they paid
            amount = eval(input("\nEnter the amount of your purchase: $"))

            #asking the user their tax rate
            taxrate = eval(input("Enter the sales tax rate as a percentage: %"))

            #itterating through the user defined function
            taxes(amount, taxrate)

            #resetting choice so that the program doesn't restart
            choice = 0

        #checking if the user chose to close the program
        while choice == 5:
            
            #thanking the user for using the financial calculator
            print("\nThank you for using the financial calculator")

            #resetting choice so that the program doesn't restart
            choice = 0

            #setting the restart variable to "N" so that the program doesn't continue to run
            restart = "N"

    #except statement not allowing for erroring out
    except:

        #telling the user that an error has occured
        print("\nAn error has occured, please try again")

        #continuing the program from where it left off
        continue


        

