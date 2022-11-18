#Cole Branston

#imports the math library for future calculations
import math

#Title of program
print("Right Triangle Program")
print("------------------------")

#Tells the user what the program does
print("\nThis program will calculate the hypotenuse, perimeter, and area\n of a right triangle")

#Asks the user what the lengths of their triangles a and b are
a = eval(input("\nEnter the length of the opposite side:  "))
b = eval(input("Enter the legnth of the adjacent side:   "))

#asks the user for the units that their measurements for their a and b are
units = input("Enter the units: ")

#calculations for the area, hypotenuse, and perimeter
hyp = math.sqrt(a**2+b**2)

area = (a*b)/2

perimeter = (a+b+hyp)

#printing the final statements including area, perimeter, and hypotenuse
print("\nThe area of the right triangle is", round(area,1), "square", units+".")
print("The perimeter of the right triangle is", round(perimeter,1), units+".")
print("The length of the hypotenuse of the right triangle is", round(hyp,1), units+".")





