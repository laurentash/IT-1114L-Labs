# Program Name: Lab1.py 
# Course: IT1114L - Lab 1 Flooring
# Name: lauren shockley
# Assignment Number: Lab 1
# Due Date: 08/21/23
# Purpose: This program takes a total of three user inputs with directions and outputs calculated float numbers that relate to the total square footage and -
    # replacement cost of the inputy room dimensions. 

RmLength = float(input("Total Room Length:")) # ->Asks user for input of the room's length
RmWidth = float(input("Total Room Width:")) # ->Asks user for input of the room's width
SqftCost = float(input("Cost of flooring per square foot:")) # ->Asks user for input of the flooring cost per square foot

def squarefeet(RmWidth, RmLength) : # ->Defining the 'squarefeet' function to calculate the square footage of the room from the user's input 
    return (RmWidth * RmLength)
    
def floorcost(squarefeet, SqftCost) : # ->Defining the 'floorcost' function to calculate the total floor replacement cost from the user's input 
    return (squarefeet * SqftCost)
    
total_sqft = squarefeet(RmWidth, RmLength)  # ->Calculated total square footage into variable for print simplicity
total_cost = floorcost(total_sqft, SqftCost)  # ->Calculated total cost into variable for print simplicity
    
print(f"Total Room Square Footage: {total_sqft}") # ->Prints output of the room's total square footage!

print(f"Total Flooring cost: ${total_cost}") # ->Prints output of the room's cost for flooring replacement!
