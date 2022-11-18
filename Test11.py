#Cole Branston 

#importing the math libary for future calculations
import math

#Title of the program
print("Rectangle Program")
print("------------------")

#telling the user what the purpose of the code is
print("\nThis program will calculate the area, perimeter, and diagonal\n of a rectangle.")

#Asking the user the length, width, and units of their rectangle 
length = eval(input("\nEnter the length of the rectangle: "))
width = eval(input("Enter the width of the rectangle: "))
units = input("Enter the units: ")

#Calculations for the area, perimeter, and diagonal_length
area = length*width
perimeter = (2*length)+(2*width)
diagonal_length = math.sqrt(length**2+width**2)

#telling the user what the area, perimeter, and diagonal length of their rectangle.
print("\nThe area of the rectangle is", round(area,2), "square", units+".")
print("The perimeter of the rectangle is", round(perimeter,2), units+".")
print("The diagnonal of a rectangle is", round(diagonal_length,2), units+".")