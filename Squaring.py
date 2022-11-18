# Name: Cole Branston
# Date: 2022/05/20
# Purpose: To square all the numbers of a list

#initializing a list
numbers = [2,4,7,10,12,15,16]

#defining a function
def squaring(x):

    #defining square and setting to the square of a number
    square = numbers[x]**2

    #returning square
    return square

#for loop itterating thorugh range of list
for x in range(len(numbers)):

    #calling function
    squaring(x)

    #defining where the varibale came from
    square = squaring(x)

    #printing the final statement
    print("The square of", numbers[x], "is", square)
