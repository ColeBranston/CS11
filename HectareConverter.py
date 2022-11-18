# Name: Cole Branston
# Purpose: Coverts hectares into acres, square metres, and squar feet
# Date: 2022/02/18

#These print statement tells the user the purpose of this program
print("\nThe hectare is a unit of area defined as 10,000 square metres (100 m by 100 m), and primarily used in the measurement of land. Before the metric system was used to measure land area, the British system used a measurement called acres.")

print("\nThis program converts hectares to acres, square metres, and square feet.")

#This asks the user how much hectares they want to convert
hct = eval(input("\nEnter the number of hectares: "))

#if the value the user inputs is less than 0, tell the user to use a positive integer, and ask again
while hct < 0:
        print("\nUse a positive integer") 
        hct = eval(input("\nEnter the number of hectares: "))


#This is the math behind the conversions
acres = hct*2.47
smetres = hct*10000
sfeet = hct*107600

#This is the final print statement that tells the user how much of each unit there inputted hectares is
print("\n",hct, "hectares is equivalent to:","\n", "   ",acres, "acres", "\n","   ", smetres, "square metres", "\n","   ", sfeet, "square feet")
