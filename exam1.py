# Exam 1 - Lauren Shockley


credithrs = int(input("Enter the number of credit hours: ")) # -> Prompt the user for the number of credit hours and residency status
residencystatus = input("Are you in-state or out-of-state? (Enter 'in-state' or 'out-of-state'): ")


in_state_rate = 296 # -> Define the tuition rates
out_of_state_rate = 1066


if residencystatus == "in-state": # -> Calculate the total tuition based on residency status
    tuitiontotal = credithrs * in_state_rate
elif residencystatus == "out-of-state":
    tuitiontotal = credithrs * out_of_state_rate
else:
    print("Invalid residency status. Please enter 'in-state' or 'out-of-state'.")
    tuitiontotal = 0  # -> Set tuition to 0 for invalid input


if tuitiontotal > 0: # -> Display the total tuition
    print(f"Your total tuition for {credithrs} credit hours as an {residencystatus} student is ${tuitiontotal}.")
