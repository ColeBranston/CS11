# Name: Cole Branston
# Date: 2022/03/23
# Purpose: determine the value of the $24.00 in each year that is a multiple of 10 from 1634 to 2014 and 2014 in Manhattan

#defining again variable in order to restart while loop
again = "Y"

#while loop for code
while again == "Y":
    #printing the title of the program
    print("Manhattan Island")
    print("-----------------")

    #telling the user what the purpose of the program is 
    print("\nIn 1634, the American Indians sold Manhattan Island for $24.00.\nIf the money had been invested, it would have grown to a very large\namount by the year 2014.")
     
    #Try except to limiting errors
    try:
        #asking the user for the interest rate
        interest = eval(input("\nEnter the interest rate (2.5 for 2.5%): "))

        #Calculating the decimal interest rate
        interest = (interest/100)+1

        #defining interest
        year = 1634

        #calculating the total value of the first nation's money
        total = 24*interest

        #Title of the listing of values by years
        print("Year     Amount".rjust(10))
        print("------   -------".rjust(10))

        #while loop for printing years and values before 2015 
        while year < 2015:

            #while loop for printing years and values every 10 years 
            if year % 10 == 0 or year == 2014:
                print(year, str(round(total,2)).rjust(10))

            #changing total and years 
            total *= interest
            year +=1

    #Try except to limiting errors
    except: 
        print("\nError, try again")

    #asking the user if they want to restart the program
    again = input("Do you to replay the program (Y/N):").upper()