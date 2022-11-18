# Name: Cole Branston
# Date: 2022/03/01
# Purpose: Calculates the BMI of a the user than makes judements accordingly

#Title of program
print("Body Mass Index (BMI) Calculator")
print("------------------------------------")

#Telling the user what BMI is
print("\nBody mass index (BMI) is a measure of the weight of a person scaled\naccording to their height. BMI is defined as the individual's body\nweight divided by the square of the height, and is almost always\nexpressed in the unit kg / m².")

#Telling the user what the formual for BMI is
print("\nThe metric formula for calculating BMI is: Weight(kg)/Height(m)²")

#Telling the user what the purpose of this program is
print("\nThis program will calculate a person's body mass index (BMI).")

#Asking the user for both their weight in kilograms and height in metres
weight = eval(input("\nEnter your weight in kilograms (kg): "))
height = eval(input("Enter your height in metres: "))

#calculations for BMI
BMI = round(weight/(height*height),2)

#printing the user's BMI
print("\nYour body mass index is: ",BMI,"kg/m².")

#Making comments according to their BMI
#Telling the user that they are starving
if BMI < 15:
    print("\nYou are in Starvation, \nyou need to be eating a lot more")
#Telling the user that they are underweight because 
elif BMI < 18.5:
    print("\nYou are underweight, \ntry to consume more calories")
#Telling the user that their BMI is 
elif BMI < 25:
    print("\nYour BMI is ideal, \ngood job")
#Telling the user that they are overweight
elif BMI < 30:
    print("\nYou are overweight, \ntry to consume less calories")
#Telling the user that they are obese
elif BMI < 40:
    print("\nYou are obese, \nstart a diet and eat less")
#Telling the user that they are morbily obese
else:
    print("\nYou are morbidly obese, \nstart a diet, eat less, see the doctor, and excersise")