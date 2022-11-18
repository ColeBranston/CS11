# Name: Cole Branston
# Date: 2022/02/22
# Purpose: Calculate the are of a triangle

#imports math library
import math

#title of the program
print("Area of Triangle Calculator")
print("---------------------------")

#tells the user what the programs purpose is
print("In geometry, Heron's formula states that the area A of a triangle\nwith sides that have lengths a, b, and c is:\nA = \u221A(s(s-a)(s-b)(s-c))\nwhere s is the semi perimeter of the triangle:\ns = (a + b + c) / 2\n\nThis program will calculate the area of a triangle using Heron's formula.  ")

#asks the user the measurements of each side
sideA = eval(input("Enter the length of side a: "))
sideB = eval(input("Enter the length of side b: "))
sideC = eval(input("Enter the length of side c: "))

#calculates the variable "s"
s = (sideA+sideB+sideC)/2

#calculations behind finding the area of a triangle using the inputted integers
area = round(math.sqrt(s*(s-sideA)*(s-sideB)*(s-sideC)), 3)

#tells the user what the area of their triangle is
print("\nThe area of the triangle is:",area)