# Name: Cole Branston
# Purpose: Determine the amount of x intercepts in a quadratic using the quadratic equation and discrimant
# Date: 2022/03/01

#Importing the math library for later calculations
import math

#Title of program
print("Quadratic Formula")
print("-------------------")

#Telling the user the purpose of the program
print("\nThis program will calculate the roots of the quadratic equation ax² + bx + c = 0 using the quadratic formula.")

#Asking the user for the a, b, and c values in their quadratic equation
a = eval(input("\nEnter the value of a: "))
b = eval(input("Enter the value of b: "))
c = eval(input("Enter the value of c: "))

#Calculating the discrimant
discrimant = b**2-4*a*c

#Checking if the discrimant is less than 0
if discrimant <0:
    #Telling the user that their are no real x intercepts
    print("\nThere are no real x intercepts")

#Checking if the discrimant is equal to 0
elif discrimant == 0:
    #calculating x1
    x1= round((-b+(math.sqrt(discrimant)))/(2*a),2)
    print("\nThe only root, X1 = ", x1)

#Checking if the discrimant is equal to anything else, A.K.A. positive
else:
    #Calculating both x intercepts
    x1= round((-b+(math.sqrt(discrimant)))/(2*a),2)
    x2= round((-b-(math.sqrt(discrimant)))/(2*a),2)
    #printing the x intercepts
    print("\nThe first root, X1 = ", x1,"\nThe second root, X2 = ", x2)

