# Program Name: Lab5.py 
# Course: IT1114/Section 1
# Student Name: Lauren Shockley
# Assignment Number: Lab 5
# Due Date: 10/2/23
# Purpose: A program that stores atributes in the Worker class and can output siad atributes when called
# Prior knowledge and majority provided materials

class Worker: # -> Object template Worker (9-49) sets atributes for different charcteristics of an employee
    def __init__(self):
        self.employeenumber = ""
        self.officenumber = ""
        self.firstname = ""
        self.lastname = ""
        self.annualsalary = 0.0

    def getemployeenumber(self):
        return self.employeenumber

    def setemployeenumber(self, x):
        self.employeenumber = x

    def getofficenumber(self):
        return self.officenumber

    def setofficenumber(self, x):
        self.officenumber = x

    def getname(self):
        return f"{self.firstname} {self.lastname}"

    def setname(self, x):
        parts = x.split()
        if len(parts) == 2:
            self.firstname, self.lastname = parts[0], parts[1]
        else:
            print("Please enter both their first and last names; e.g. 'Herbie Hancock'.")

    def getannualsalary(self):
        return self.annualsalary

    def setannualsalary(self, x):
        self.annualsalary = x

    def getmonthlysalary(self):
        return self.annualsalary / 12

    def __str__(self):
        return f"Employee name: {self.firstname} {self.lastname}, Office Number: {self.officenumber}, Yearly Salary: ${self.annualsalary:.2f}"


test_employee = Worker() # -> 53-57 Sets the different atributes for the test employee
test_employee.setemployeenumber("404678770")
test_employee.setofficenumber("54185")
test_employee.setname("Mary Jane")
test_employee.setannualsalary(75123)

print(test_employee) # -> Prints the contained information for the test emnployee
