# Program Name: Lab4.py 
# Course: IT1114/Section 1
# Student Name: Lauren Shockley
# Assignment Number: Lab 4
# Due Date: 9/25/2023
# Purpose: A program that determins the final total for a bill based off of party size and bill inputs!
# Prior knowledge and provided materials!

def finaltotal(beforetip, partysz): # -> Function that determines the autograd  by party size (true/false)
    if partysz <= 5:
        tippercent = float(input("Enter the desired tipping percentage: "))
    else:
        tippercent = 18
    
    tipamount = (beforetip * tippercent) / 100
    finalamt1 = beforetip + tipamount  
    return finalamt1

def main(): # -> 'Main' function that asks for inputs and outputs the final total after determinig autograd
    beforetip = float(input("Enter the bill total bvefore tip: "))
    partysz = int(input("Enter the party size: "))
    
    final_total = finaltotal(beforetip, partysz)  
    
    print(f"Final total including tip percent or autograd is: ${final_total:.2f}")

if __name__ == "__main__":
    main()
