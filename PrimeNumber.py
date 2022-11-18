# Name: Cole Branston
# Date: 2022/04/11
# Purpose: This program will take an input by the user and calculate if it is prime or not

#defining the bool variable and the again variable to restart the program
again = "Y"
bool = True
#main loop that starts if again = "Y" which allows the program to restart
while again == "Y":
    #try statement that doesn't allow for an error out
    try:
        #printing the title of the program
        print("Prime Number Calculator".rjust(10))
        print("-----------------------".rjust(10))

        #Telling the user the purpose of the program
        print("This program will determine if a number entered by the user is a\nprime number or not. Recall that a number is prime if it cannot\nbe evenly divisible by any number from 2 to one less than the number,\notherwise it is a composite number")

        #asking the user for a number input and defining it as pnum
        num = int(input("\nEnter your number to determine if it is a prime number: "))

        #avoiding users entering a negative integer
        while num <= 0:
            print("\nEnter an actual valid number (number greater than 0)")
            num = int(input("\nEnter your number to determine if it is a prime number: "))
        #initializing bool to reset variable
        bool = True
        #loop that checks if a number is prime or not
        for x in range(2, num):
            #if the num's remainder of x is 0 than it is not a prime number, making bool false
            if num%x ==  0:
                bool = False
                break
            
        #if bool true than tell user that their number is prime
        if bool == True:
            if num == 1:
                print("\n1 is not a prime number")
            else:
                print("\nThis is a prime number")

        #if bool false than tell user that their number isn't prime
        elif bool == False:
            print("\nThis number is NOT a prime number")

        #asking the user if they want to restart the program
        again = input("\nDo you want to restart the program (Y/N):").upper()

#except statement that tells the user that an error has occurred and asking them if they want to restart the program
    except:
        print("\nError in values, Try Again")
        again = input("\nDo you want to restart the program (Y/N):").upper()
