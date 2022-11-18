# Name: Cole Branston
# Date: 2022/04/27
# Purpose:enter the three colours of a resistor and then print the value of the resistor.

# initialzing the again variable in order restart the program
again = "Y"

# main while loop containing the program that can restart
while again == "Y":

    # try statement that doesn't allow for errors
    try:
        # initializing lists
        colourlist = [
            "BLACK",
            "BROWN",
            "RED",
            "ORANGE",
            "YELLOW",
            "GREEN",
            "BLUE",
            "VIOLET",
            "GREY",
            "WHITE",
        ]

        # title of program
        print("\nResistors")
        print("---------")

        # telling the purpose of the program
        print(
            "\nElectronic resistors have their values marked by three painted colour bands (a\ncolour code).\nThe values of the colours are as follows:\nBLACK – 0 BROWN – 1 RED – 2\nORANGE – 3 YELLOW – 4 GREEN – 5\nBLUE – 6 VIOLET – 7 GREY – 8\nWHITE – 9\nThe first two colours are combined to create a two-digit number.\nThe third colour is a power of 10.\nFor example, a RED-BROWN-ORANGE resistor has the value 21 * 10^3 ohms = 21000 ohms."
        )

        # asking the user for their colour bands and replacing the hyphens with spaces
        colours = (
            input("\nEnter the colour bands separated by a hyphen: ")
            .upper()
        )

        # splitting the users input into a list
        coloursinput = colours.split("-")

        # definging the ohms, num1, and num2 varibles, and doing calculations
        num1 = str(colourlist.index(coloursinput[0])) + str(colourlist.index(coloursinput[1]))
        num2 = colourlist.index(coloursinput[2])
        ohms = (int(num1) * 10 ** colourlist.index(coloursinput[2]))

        # telling the user the resistance of their colour bands
        print(
            "\nA",
            colours,
            "resistor has the value",
            num1,
            "* 10^",
            num2,
            " = ",
            ohms,
            "ohms",
        )

        # asking the user if they want to restart the program
        again = input("\nDo you want to restart the program? (Y/N): ").upper()

    # except statement that doesn't allow for erroring out
    except:
        # telling the user that an error has occured
        print("\nAn error has occured, please try again")
        # continuing the program where it left off
        continue
