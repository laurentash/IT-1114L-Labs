# Program Name: Exam3.py 
# Course: IT1114/Section 1
# Student Name: Lauren Shockley
# Assignment Number: Exam 3
# Due Date: 12/04/23
# Purpose: A program receives input for a measure of length and unit, validates the data and then calculates the resultant conversion into mi or km.
# Provided materials and research, some prior knowledge. 


def floatinput(prompt): # -> While loop that validates the float length value
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Sorry! Please enter a correct float number (1,2.0, 6.7).")

def unitinput(prompt): # -> While loop that validates the length unit value
    while True:
        unit = input(prompt)
        if unit.upper() in {'KM', 'MI'}:
            return unit.upper()
        else:
            print("Oops! Please enter a measure unit (KM or MI).")

def kmconvert(km): # -> Calcuation that converts kilometers to miles
    return km * 0.6214

def miconvert(miles): # -> Calculation that converts miles to kilometers 
    return miles * 1.6093

def main(): # -> Fucnction that requsts input for length and unit, and outputs the correct sting and value
    distance = floatinput("Please enter a float number for length: ")
    unit = unitinput("Please enter a unit of measure (KM or MI): ")

    if unit == 'KM':
        convertdistance = kmconvert(distance)
        print(f"The converted distance from KM is {convertdistance:.4f} Miles")
    elif unit == 'MI':
        convertdistance = miconvert(distance)
        print(f"The converted distance from MI is {convertdistance:.4f} Kilometers")

if __name__ == "__main__":
    main()
