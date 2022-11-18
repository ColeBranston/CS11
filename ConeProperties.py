# Name: Cole Branston
# Date: 2022/02/22
# Purpose: Calculates the surface area and volume of a cone

#importing the math library for different calculations concerning pi
import math

#title of program
print("Cone Properties")
print("------------------------")

#telling the user what the program does
print("\nThis program will calculate the volume and surface area of a cone. ")

#asking the user for the raius and height of their cone
r = eval(input("\nEnter the radius of the Cone: "))
h = eval(input("Enter the height of the Cone: "))

#calculating the surface area and volume of the user's cone
surface_area = round((math.pi*(r**2))+(math.pi*r)*(math.sqrt((r**2)+(h**2))),2)

volume = round((1/3)*(math.pi*(r**2)*h),2)

#printing the final statement that tells the user the volume and surface area of their cone.
print("\nThe volume of the cone is:", volume, "units cubed.\nThe surface area of the cone is:", surface_area, "square units.")
