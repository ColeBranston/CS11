# Name: Cole Branston
# Date: 2022/04/25
# Purpose: This program randomly picks one word from each list (plural nouns, verbs, singular nouns) and creates a potentially comical sentence.

#importing random 
import random 

# initializing the again variable in order to restartt my program
again = "Y"

#main while loop containing the program that allows for restart
while again =="Y":

    #try statement not allowing for erroring out 
    try: 
        
        #initializing lists
        plurals = []
        verbs = []
        singulars = []

        #opening and reading the plurals.txt
        pluralsdoc = open("plurals.txt", "r")
        pluralsline = pluralsdoc.readline()

        #checking if a line isn't blank, adding to the list, reading next line
        while pluralsline != "":

            pluralslinestripped =pluralsline.rstrip("\n")
            plurals.append(pluralslinestripped)
            pluralsline = pluralsdoc.readline()
        
        #closing doc
        pluralsdoc.close()

        #opening and reading verbs.txt
        verbsdoc = open("verbs.txt", "r")

        verbsline = verbsdoc.readline()

        #Checking if the line of the verbs doc is not blank
        while verbsline != "":
            #strippin the line of\n, adding to a list, and reading the next line
            verbslinestripped =verbsline.rstrip("\n")
            verbs.append(verbslinestripped)
            verbsline = verbsdoc.readline()
        #closing the verbs doc
        verbsdoc.close()

        #opening singulars.txt
        singularsdoc = open("Singulars.txt", "r")

        #reading the singular doc
        singularline = singularsdoc.readline()

        #checking if the singular doc's line is not blank
        while singularline != "":

            #stripping the line of \n, adding it to a list, and reading the next line
            singularlinestripped = singularline.rstrip("\n")
            singulars.append(singularlinestripped)
            singularline = singularsdoc.readline()

        #closing the singulars doc
        singularsdoc.close()

        #title of program
        print("MadLib")
        print("------")

        #telling the user what the program looks like
        print("\nThis program randomly picks one word from each list\n(plural nouns, verbs, singular nouns) and creates a\npotentially comical sentence.")

        #randomly choosing a word through the different docs
        print("\n"+ str(random.choice(plurals)), random.choice(verbs), random.choice(singulars))

        #asking the user if they want to restart the program
        again = input("\nDo you want to restart the program? (Y/N): ").upper()

    #except statement not allowing for the user to error out
    except:
        #telling the user that an error has occured
        print("\nAn Error has occurred")
        #continuing the program
        continue