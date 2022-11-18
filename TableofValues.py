# Name: Cole Branston
# Date: 2022/04/22
# Purpose: program that creates a table of values for the equation y = 3*x**2

#subtitles telling the user what side is x and what side is y in the calculations
print("X".rjust(10), "Y".rjust(15))
print("---".rjust(11), "---".rjust(15))

#loop changing x by 5 from 5 to 50
for x in range(5, 51, 5):
    #formula for calculations
    y = 3*x**2
    #printing the x to y calculations
    print(str(x).rjust(10), str(y).rjust(15))

#loop changing x by 10 from 60 to 100
for x in range(60, 101, 10):
    #formula for calculations
    y = 3*x**2
    #printing the x to y calculations
    print(str(x).rjust(10), str(y).rjust(15))
    