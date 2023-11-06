# Program Name: Lab8.py 
# Course: IT1114/Section 1
# Student Name: Lauren Shockley
# Assignment Number: Lab 8
# Due Date: 11/6/23
# Purpose: Program that enforces a specific user input fornat and displays the corresponding year and date. 
# Knowledge and majority provided materials

def validmonth(month): # -> Function 'validmonth' validates correct input for month integer
    return 1 <= month <= 12

def validyear(year): # -> Function 'validyear' validates correct input for year integer
    return 1900 <= year <= 2023

# -> 16-17 Initializes the input variables to zero
birthmonth = 0
birthyear = 0

# -> 20-30 Include functions that print value error messages through while loops if the input is not correctly formatted
while not validmonth(birthmonth):
    try:
        birthmonth = int(input("Enter your birth month (1-12): "))
    except ValueError:
        print("No, please enter a valid month (corresponding number) between 1 and 12.")

while not validyear(birthyear):
    try:
        birthyear = int(input("Enter the birth year (1900-2023): "))
    except ValueError:
        print("No, please enter a valid year (number) between 1900 and 2023.")

print(f"The birth date is: {birthmonth:02}/{birthyear}") # -> Prints the formatted resultant
