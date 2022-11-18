# Name: Cole Branston
# Date: 2022/04/25
# Purpose: sort values in a text document and answer different questions

#initializng again in order to restart the program later on
again = "Y"

#main while loop containg main program and allowing for restart
while again == "Y":

    try: 
        print("Values.txt File Information")
        print("---------------------------")
        # opening the values.txt file
        inFile = open("Values.txt",'r')

        #reading the lines in the text document
        line = inFile.readline()

        #Creating a empty list
        numbers = []

        #repeat as long as the line is not empty
        while line != "":
            line = line.rstrip("\n")
            #append adds an object to the end of the list
            numbers.append(int(line))

            #Reading the next line
            line = inFile.readline()
        #closing the text document
        inFile.close()

        #telling the user what the original values in the text document were
        print("\nThe original numbers are", numbers)
        #sorting the appended values
        numbers.sort()
        #telling the user what the sorted version of the values in the text document are. Sorted by least to greatest
        print("\nThe sorted numbers are: ", numbers)

        #telling the user the amount of numbers in the list, the smallest number in the list, the largest number in teh list, the average of the values in the list, and the median of the values that are in the list.
        print("\nThe number of numbers in the list are: ", len(numbers))
        print("The smallest number in the list is:", numbers[0])
        print("The largest number in the list is: ", numbers[-1])
        print("The average of the values in the list is: ", sum(numbers)/len(numbers))
        print("The median of the values in the list is: ", numbers[len(numbers)//2])
        
        #asking the user if they want to restart the program
        again = input("\nDo you want to restart the program? (Y/N): ").upper()

    except:
        print("\nAn error has occurred")
        continue

