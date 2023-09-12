# Program Name: Lab2.py 
# Course: IT1114/Section 1
# Student Name: Lauren Shockley
# Assignment Number: Lab 2 
# Due Date: 9/4/2023
# Purpose: This program takes an input from end user and outputs five relating calculations for cost. 
# Prior knowledge and provided materials!
 
particnum = float(input("Number of Participants: ")) # -> Takes inpu for subsequent calculations 


def foodcost(particnum): # -> Function for sandwich costs pre tax and discount
    return particnum * 7.99

def discountedtotal(particnum, cost): # -> Function determining whether to administer discount or not
    if particnum > 50:
        return cost * 0.15  # 15% discount
    else:
        return 0

def taxcalc(particnum): # -> Funtion for calculating tax cost
    return particnum * 7 / 100  

cost = foodcost(particnum) # -> Assigning value to variable
discount = discountedtotal(particnum, cost) # -> Assigning value to variable
situation = cost - discount # -> Assigning value to variable

finaltotal = situation + taxcalc(particnum) # -> Assigning value to variable

print(f"Participant total: {particnum} ") # -> Prints the number of participants 
print(f"Total sandwich cost before tax and discount: {cost}") # -> Prints the cost of sandwiches pre tax and discount
print(f"Total discounted amount: {discount}") # -> Prints discounted amount
print(f"Total with discount applied: {situation}") # -> Prints the total with discount applied
print(f"Gross overall total with tax and discount: {finaltotal}") # -> Prints the total with discount and tax applied