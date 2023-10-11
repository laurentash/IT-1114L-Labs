# Program Name: Lab6.py 
# Course: IT1114/Section 1
# Student Name: Lauren Shockley
# Assignment Number: Lab 6
# Due Date: 10/9/23
# Purpose: A program that 
# Prior knowledge and majority provided materials

rainfallstats = [] # -> Initializing the empty list to store monthly rainfall

for month in range(1, 13): # -> Loop that asks for 12 months worth of input
    while True:
        try:
            rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
            if rainfall < 0:
                print("Sorry! Rainfall must be a positive number or zero.")
                continue
            rainfallstats.append(rainfall)
            break
        except ValueError:
            print("Not right. Please enter a valid number!")

totalrainfall = sum(rainfallstats) # -> Variables to do simple calculations with the inputted values
averagerainfall = totalrainfall / 12
highestrainfall = max(rainfallstats)
lowestrainfall = min(rainfallstats)

# -> Displays the resulting statistics from inputs and calculations 
print("\nAnnual ainfall statistics for the year:")
print(f"Total annual rainfall: {totalrainfall} inches")
print(f"Average rainfall per month: {averagerainfall:.2f} inches")
print(f"Highest recorded rainfall: {highestrainfall} inches (Month {rainfallstats.index(highestrainfall) + 1})")
print(f"Smallest recorded rainfall: {lowestrainfall} inches (Month {rainfallstats.index(lowestrainfall) + 1})")
