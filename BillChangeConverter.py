# Name: Cole Branston
# Date: 2022/02/02
# Purpose: Convert a sum of money into fives, toonies, loonies, quarters, dimes, nickels, and pennies

#title of program
print("Bill and Change Converter")
print("-------------------------------")

#telling the user what the purpsoe of the program is
print("\nThe purpose of this program is to convert any sum of money between $0.01 - $10 into bills and change")

#asking the user for the amount of money they want to convert
money = eval(input("\nHow much money do you wish to convert in dollars ($): "))

#calculating how much of each bill or coin is needed to split the user oringial sum of money
fives = round(money//5)
money -= fives*5

toonies = round(money//2)
money -= toonies*2

loonies = round(money//1)
money -= loonies*1

quarters = round(money//0.25)
money -= quarters*0.25

dimes = round(money//0.1)
money -= dimes*0.1

nickels = round(money//0.05)
money -= nickels*0.05

pennies = round(money*100)

#initializing the printed variables and setting the base appearances as nothing
fives_display = ""
toonies_display = ""
loonies_display = ""
quarters_display = ""
dimes_display = ""
nickels_display = ""
pennies_display = ""

#checking if the variables do exist and setting the displayed characters as their amount in a string and setting the words according to the singular or plural amount
# If the amount is equal to zero than nothing happens and the displayed amount remains as nothing when initialized above.
if fives > 1:
    fives_display = str(fives)+" fives, "

elif fives == 1:
    fives_display = str(fives)+" five, "

if toonies > 1:
    toonies_display = str(toonies)+" toonies, "

elif toonies == 1:
    toonies_display = str(toonies)+" toonie, "

if loonies > 1:
    loonies_display = str(loonies)+" loonies, "

elif loonies == 1:
    loonies_display = str(loonies)+" loonie, "

if quarters > 1:
    quarters_display = str(quarters)+" quarters, "

elif quarters == 1:
    quarters_display = str(quarters)+" quarter, "

if dimes > 1:
    dimes_display = str(dimes)+" dimes, "

elif dimes == 1:
    dimes_display = str(dimes)+" dime, "

if nickels > 1:
    nickels_display = str(nickels)+" nickels, "

elif nickels == 1:
    nickels_display = str(nickels)+" nickel, "

if pennies > 1:
    pennies_display = str(pennies)+" pennies"

elif pennies == 1:
    pennies_display = str(pennies)+" penny"

#printing the final statement using the displayed variables in order to tell the user the bills and change they would get from their orginal amount of money
print("\n","requires",fives_display+toonies_display+loonies_display+quarters_display+dimes_display+nickels_display+pennies_display)
