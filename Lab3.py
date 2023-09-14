# Program Name: Lab3.py 
# Course: IT1114/Section 1
# Student Name: Lauren Shockley
# Assignment Number: Lab 3
# Due Date: 9/11/2023
# Purpose: This program outputs seven years worth of incrementally increasing tuitionn prices and their corresponding years. 
# Prior knowledge and provided materials!

tuitioncost = 6450 # -> Sets variable tuitioncost as initial cost of yearly tuition


for sevenyears in range(2018, 2025): # -> For loop calculating the increasing tuition cost. 
    print(f"For {sevenyears} the tuition per semester is: ${tuitioncost:.2f}") #-> Prints final cost per year
    
    tuitioncost *= 1.035  # -> Sets new incremental calculation up for the outputs
