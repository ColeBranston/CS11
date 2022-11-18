
#importing random for later use
import random

#initializing the list
listgeneratorlist = []

#defining the listgenerator function
def listgenerator(amount):

    #checking if the amount is greater than 0
    while amount > 0:

        #itterating throught he range that the user set
        for x in range(0, amount):

            #adding the random number to a list
            listgeneratorlist.append(random.randint(1,100))

        #printing the final list
        print(listgeneratorlist)
        break

    #checking if the amount is less than 0
    while amount < 0:

        #asking the user for how long they want their list to be
        amount = int(input("How long of a list do you want?: "))

#defining the factor checker function
def factorchecker(num1, num2):

    #checking if the smaller number is less than the larger number
    while num2 < num1:

        #checking if num 2 is a factor of num 1
        if num1 % num2 == 0:

            #telling the user that number 2 is a factor of number 1
            print("Your smaller number is a factor of your larger number")

        #telling the user that the smaller number is not a factor of the larger number
        else: 
            print("Your smaller number is not a factor of your larger number")
            
    #checking for any user errors
    while num2 > num1 or num1 < 0 or num2 < 0:

        #resasking the user for their numbers
        num1 = int(input("\nWhat is the larger number?:"))
        num2 = int(input("What is your smaller number?: "))

#main while loop
while True:

    #try statement not allowing for erorring out
    try:

        #printing the interactable menu
        print("1.List Generator\n2. Factor Check\n3. Exit Program")

        #asking the user what function they want to run
        choice = int(input("\nWhat is your choice? (1,2, or 3): "))

        #if choice 1 is 1 
        if choice == 1:

            #asking the user for the length of the list
            amount = int(input("How long of a list do you want?: "))

            #calling the function
            listgenerator(amount)

        #Checking if choice is 2
        elif choice == 2:

            #asking the user for the num1 and num2
            num1 = int(input("\nWhat is the larger number?:"))
            num2 = int(input("What is your smaller number?: "))

        #checking the choice is 3
        elif choice == 3:

            #telling the user goodbye
            print("Goodbye")

            #breaking the loop
            break

    #except statement not allowing for erroring out
    except:

        #telling the user that an error has occured
        print("\nAn error has occured")

        #continueing the program as it left off
        continue