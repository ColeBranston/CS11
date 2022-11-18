# Name: Cole Branston
# Date: 2022/03/03
# purpose: calculates the cost of printing paper copies: prompts the user for the number of copies to print and then displays the price per copy, cost before discount, discount, price after discount, and total cost.

#title of the program
print("Printing Price Calculator")
print("-------------------------")

#telling the user what the purpose of the program is
print("\nPrinting prices are based on the number of copies to be printed\n0 - 499 copies   $0.30 per copy \n500 - 749 copies   $0.28 per copy \n750 - 999 copies   $0.27 per copy \n1000 copies or more  $0.25 per copy ")
print("The purpose of this program is to calculate the cost of printing prices")
#asking the user for the number of copies they want and if they get an employee discount 
copies = eval(input("\nEnter the number of copies you would like: "))
ediscount = input("Are you eligible for the employee discount (Y or N): ").upper()

#determining the user's price per copy based on the amount of copies they want 
if copies <= 499:
    price = 0.30

elif copies <= 749:
    price = 0.28

elif copies <= 999:
   price = 0.27

else:
    price = 0.25

#telling the user what their price per copy will be
print("\nou will be charged $", round(price,2), "per copy.")

#calculating what the users cost will be without tax or discount
price_before_discount = copies*price

#telling the user what their price before discount and tax is 
print("\nPrice before discount:            $", round(price_before_discount,2))

#determining the discount the user gets
if ediscount == "Y":
    discount = price_before_discount*0.1

else: 
    discount = 0

# printing the discount
print("Discount:                         $",round(discount,2))

#calculating the price after discount
price_after_discount = price_before_discount-discount

#telling the user what the cost is after discount
print("Price after discount:             $", round(price_after_discount,2))

#calculating the tax that will be added on the price after discount
HST = 0.13*price_after_discount

#printing the tax
print("HST                               $", round(HST,2))
print("--------------------------------------------")

#calculating the toal cost
total = round(price_after_discount + HST,2)

#telling the user what their total cost will be
print("Total Price                       $", total)