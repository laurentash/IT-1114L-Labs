# Program Name: Lab7.py 
# Course: IT1114/Section 1
# Student Name: Lauren Shockley
# Assignment Number: Lab 7
# Due Date: 11/3/23
# Purpose: Program that takes string input and outputs the number of instances of a entered word. 
# Knowledge and majority provided materials


def countword(sentence, word): # -> Function that counts inputted word with for in loop after splitting
    inptwords = sentence.split()
    count = 0

    for w in inptwords:
        if w == word: # -> Checks for word/input sameness
            count += 1

    return count

# -> 26-27 Gets inputs for the sentence and word for counting
inptsentence = input("Your sentence: ")
inptword = input("The word for counting: ")

occurrences = countword(inptsentence, inptword) # -> Calls countword to count occurences

print("Number of word occurences:", occurrences) # -> Prints the final resulted of counted words after input

