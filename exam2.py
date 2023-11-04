# Program Name: Exam2.py 
# Course: IT1114/Section 1
# Student Name: Lauren Shockley
# Assignment Number: Exam 2
# Due Date: 10/23/23
# Purpose: A program that calulates the volume of an object (water tower) after receiving inputs. 
# Prior knowledge and also provided materials


import math

def spherevolume(radius): # -> Fuction that initially calculates teh volume of the sphere
    return (4/3) * math.pi * (radius ** 3)

def cylindervolume(radius, height): # -> Fuction that finds the volume of the cylindrical portion
    return math.pi * (radius ** 2) * height

sphererad = float(input("Input the radius for the sphere portion: ")) # -> Gets input for sphere portion

# -> 21-22 Inputs for the radius and height for the cylinder portion
cylinderrad = float(input("Input the radius for the cylinder portion: "))
cylinderheight = float(input("Input the height for the cylinder portion: "))

# -> 25-26 Subsequent volume caluclations
spherevol = spherevolume(sphererad)
cylindervol = cylindervolume(cylinderrad, cylinderheight)

totalvol = spherevol + cylindervol # -> Final volume calculation

print(f"Total volume of the water tower provided is: {totalvol}") # -> Outputs the final volume
