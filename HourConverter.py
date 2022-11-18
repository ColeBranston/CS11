# Name: Cole Braston
# Date: 2022/05/02
# Purpose: Uses a user-defined function that converts a persons yearly salary into daily, weekly, and monthly salaries

#initializing the again varible in order to later restart the program and start the main while loop
again = "Y"

#defining the user defined function
def converter(oghours):
    #calculations for conversions
    weeks = oghours//168
    days = (oghours%168)//24
    hours = (oghours%168)%24

    #retuning calculations
    return weeks, days, hours

#main while loop contaiing program and allowing for restart
while again == "Y":
    #try statement not allowing for erroring out
    try:
        #title of program
        print("Hour Converter")
        print("--------------")

        #asking the user the amount of hours they want to convert
        oghours = int(input("\nEnter the hours: "))

        #finalizing variables allowing them to be used
        weeks, days, hours = converter(oghours)

        #telling the user the conversions from the error 
        print("\n", oghours,"hours is", weeks, "weeks", days, "days, and", hours, "hours") 

        #asking the user if they want to restart the program
        again = input("Do you want to restart the program ? (Y/N): ").upper()

    #eccept statement not allowing for erroring out
    except:
        #telling the user that an error has occured
        print("\nAn error has occured, please try again")
        #continuing the program from where it left off
        continue




