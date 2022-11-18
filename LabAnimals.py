# Name: Cole Branston
# Date: 2022/03/25
# purpose: determine when the population of animals will outgrow the food supply in an environment 

#Defining variables (again allows for restart)
again = "Y"
hour = 1

#Main while loop allowing for my try and except to work 
while True:

    #Secondary while loop for the whole program 
    while again == "Y":
        #try statement allowing for no erroring out
        try:
            #Title of program
            print("Lab Animals")
            print("-----------")

            #Telling the user the purpose of this program
            print("\nLab animals will double in population every hour. \nThis program will determine when the population will outgrow the food supply. ")

            #asking the user for the initial population, initial food, and food added in order to make calculations
            initialpop = round(eval(input("\nEnter the initial animal population: ")))
            initialfood = round(eval(input("Enter the initial food supply: ")))
            foodadded = round(eval(input("Enter the amount of food added each hour: ")))

            #Titles for information organization
            print("\nHour  Animals At Start   Food At Start   Food At End  Animals At End ".rjust(10))
            print("----  ----------------   -------------   -----------  --------------")

            #while loop allowing for the printing of the initial pop, initial pop, second pop, or second food. 
            while initialpop <= initialfood:
                secondpop = initialpop*2
                secondfood = initialfood+foodadded-initialpop
                print(str(hour).rjust(10) , str(initialpop).rjust(10), str(initialfood).rjust(10), str(secondfood).rjust(10), str(secondpop).rjust(10))
                hour += 1
                initialpop *= 2
                initialfood=secondfood
            
            #printing the final statement answering the question, "how long will the animals take to run out of food" 
            if initialpop>initialfood:
                print("\nThe animals will outgrow the food supply after".rjust(10), hour-1, "hours.".rjust(10))

            #asking the user if they would like to restart the program
            again = input("Do you want to restart the program (Y/N): ").upper()

        #making it impossible to error out
        except: 
            #Telling the user that their is an error and asking if they want to restart the program 
            print("\nError try again")
            again = input("\nDo you want to restart the program (Y/N): ").upper()