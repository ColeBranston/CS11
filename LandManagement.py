# Name: Cole Branston
# Date: 2022/03/29
# purpose: Calculate the time it takes for Canada's top soil to erode.

#defining variables (again for restart of program)
again = "Y"

#main loop for program, can restart when the user wants it to
while again=="Y":
    #try statement not allowing for error out (even though there isn't any input)
    try:
        #title of program
        print("Land Management")
        print("---------------")

        #informing the user of the content of the program
        print("\nCareless land management causes approximately 1 percent of the topsoil to erode\neach year. It is then lost forever, since it takes nature approximately 500 years\nto produce 2.5 cm of topsoil. At 9 cm the topsoil is so shallow that crops cannot\nbe grown on a large scale. Canada has about 30 cm of topsoil.")

        #informing the user of the purpose of the program
        print("This program will calculate how many years it will take for the depth to be reduced to 9 cm.")

        #headers for listing of years and soil depth (organization)
        print("Year", "Soil".rjust(10))
        print("------","-------".rjust(10))

        soil = 30
        year = 2012
        #while loop for calculatting soil depth and year
        while soil >= 9:
            print(year, str(round(soil,2)).rjust(10))
            year += 1
            soil= soil*0.99+0.005

        #if statement responsible for outputting the last line of the table/list
        if soil <= 9:
                print(year, str(round(soil,2)).rjust(10))

        #else statement for ending if statement
        else: 
            pass

        #informing the user when the crops are unable to be grown
        print("\nCrops are unable to be grown in", year)

        #prompting the user if they want to restart the program
        again = input("\nDo you want to restart the program (Y/N): ").upper()
    except:
        #informing the user that an error has occured
        print("\nError, restart the program")

        #prompting the user if they want to restart the program
        again = input("\nDo you want to restart the program (Y/N): ").upper()


