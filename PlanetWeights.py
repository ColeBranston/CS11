# Name: Cole Branston
# 2022/03/22
# Purpose: prints out a titled table that can be used to convert Earth kilograms to weights on three other planets.

#Defining again so that the loop can start
again = "Y"

#while loop where I put all of my code
while again == "Y":

    #try statement that limits possible errors
    try:

        #telling the user the title of the program
        print("Weights on other planets")
        print("--------------------------")

        #Telling the user what the purpose of the program is 
        print("\nThis program will print out a table that converts weights on Earth to the weight on the \n Earth's Moon, Mars, and Venus.")

        #asking the user for the lower and higher earth weights in kilograms
        weight1 = eval(input("\nEnter the lower kilogram Earth weight: "))
        weight2 = eval(input("Enter the higher kilogram Earth weight: "))
    
        #subtitles for table that organize data
        print("\nEarth (kg)".rjust(10),"Earths's Moon".rjust(10), "Mars".rjust(8)," Venus".rjust(8))
        print("---------".rjust(10), "------------".rjust(10), "-----------".rjust(10),"--------".rjust(8))

        #while loop allowing for calculations using changing earth weights
        while weight1 != weight2 + 1 and weight1 > 0 and weight2 > 0:
            moonw = round(weight1*0.166,3)
            marsw = round(weight1*0.377,3)
            venusw = round(weight1*0.907,3)

            #printing the calcuations of the weights of Earth's oon, Mars, and Venus
            print(str(weight1).rjust(10), str(moonw).rjust(10), str(marsw).rjust(10), str(venusw).rjust(10))
            weight1 += 1

    #except statment limtingposible errors
    except:
        print("\nError, use integer number")


    #asking the user if they want to repeat the code (redefining the variable so that the program will repeat)
    again = input("\nDo you want to run the program again (Y/N): ").upper()

