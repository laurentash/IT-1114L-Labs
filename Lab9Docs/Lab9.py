# Program Name: Lab9.py 
# Course: IT1114/Section 1
# Student Name: Lauren Shockley
# Assignment Number: Lab 9
# Due Date: 11/19/23
# Purpose: Program that take data from an input file, preforms calculations with given data and then writes them to output file. 
# Previous knowledge, provided materials, and some research. 

def calstats(inputfilep, outputfilep): # -> calstats function 
    try:
        
        with open(inputfilep, 'r') as inputfile: # -> Opens the input file to read data
            numbers = [int(line.strip()) for line in inputfile] # -> Converts data input to integers

        # -> 17-19 Calculates the count, sum of numbers, and average number between inputs.
        count = len(numbers)
        totalsum = sum(numbers)  
        avg = totalsum / count

        with open(outputfilep, 'w') as outputfile:# -> Opens the output file for writing the calculated data
            outputfile.write(str(count) + '\n')
            outputfile.write(str(totalsum) + '\n')
            outputfile.write(str(avg) + '\n')

        print("Count, sum and total average written to file:", outputfilep) # - > Prints completion message when done

    # -> 28-31 Exception handling and satisfying try block
    except FileNotFoundError:
        print("The input file is not found!")
    except Exception as e:
        print("An error occurred:", str(e))

calstats(r'C:\Users\lshockl1\Documents\GitHub\IT-1114L-Labs\Lab9Docs\input.txt', r'C:\Users\lshockl1\Documents\GitHub\IT-1114L-Labs\Lab9Docs\output.txt')
# |-> Calls function! Viola!