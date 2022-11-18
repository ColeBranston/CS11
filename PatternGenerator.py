# Name: Cole Branston
# Date: 2022/04/08
# Purpose: Program asks user for size of pattern to generate, and the program generates that pattern

#iniitializing again to allow the program to restart
again = "Y"

#main while loop that contains the program and allows for it to restart 
while again == "Y":
    #try statment not allowing for erroring out
    try:
        #defining the varibale again which allow for the programs restart
        again = "Y"
        #outputting the title of the program
        print("Pattern Generator".rjust(10))
        print("-----------------".rjust(10))

        #telling the user the purpose of the program
        print("\nThis program will generate a  half diamond pattern")

        #asking the user what the size of their pattern is
        size = int(input("\nEnter the size of the pattern: "))

        #if statement that checks the size of the pattern of the user inputted
        if size > 0 and size < 10:
            #printing the first half of the pattern
            for x in range(0, size+1):
                print(x*str(x))
            #printing the second half of the pattern
            for z in range(size-1, 0, -1):
                print(z*str(z))
        #if the values inputted were invalid, tell the user that an error has occurred and that the values inputted need to be in the range between 1 and 9
        else: 
            print("\nerror, Values have to be 1-9")
        #asking the user if they want to restart the program
        again = input("Do you want to restart the program (Y/N): ").upper()

    #except statement not allowing for the user to error out
    except:
        #telling the user that an error has occured
        print("\nError, restart program, values incorrect")
        #asking teh suer if they want to restart the program
        again = input("Do you want to restart the program (Y/N): ").upper()