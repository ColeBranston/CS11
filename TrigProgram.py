# Name: Cole Branston
# Date: 2022/02/22
# purpose: to calculate the different angles and sides of a triangle using user inputted data

#imports math library for purposes of math and formulas
import math

#title of the program
print("Trig Program")
print("--------------")

#Telling the user what the purpose of this program is
print("\nThis program calculates the different angles and sides (angle C and sides c and b) of a triangle using user input")

#asking the user for the measurement of Side A, angle A, and Angle B of their triangle
sideA = eval(input("\nWhat is the measure of side a in cm: "))
angleA = eval(input("What is the measure of angle A in degrees: "))
angleB = eval(input("What is the measure of angle B in degrees: "))

#calculations for angle C
angleC = round(180-(angleA+angleB),2)

#converting degrees into radians as trig ratios only work with radians on python
angleA = math.radians(angleA)
angleB = math.radians(angleB)

#calculations for side B
sideB = round(sideA*(math.sin(angleB))/(math.sin(angleA)),2)

#turning angle C into radians as trig ratios only work with radians
angleC1 = math.radians(angleC)

#Calculating side C
sideC = round(sideA*(math.sin(angleC1))/math.sin(angleA),2)

#printing final statement in order to tell the user what the measurements of Angle C, side b, and side c are
print("\nIn your triangle: \nAngle C =",angleC,"\nSide b =",sideB, "\nSide c =", sideC)