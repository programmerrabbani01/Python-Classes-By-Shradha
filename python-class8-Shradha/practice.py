# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

""" 
# Answer:

class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        
    def calculate_average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3
    
    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Marks in Subject 1: {self.marks1}")
        print(f"Marks in Subject 2: {self.marks2}")
        print(f"Marks in Subject 3: {self.marks3}")
        print(f"Average Marks: {self.calculate_average():.2f}")
        
# Collect user input
name = input("Enter the student's name: ")
marks1 = int(input("Enter marks for Subject 1: "))
marks2 = int(input("Enter marks for Subject 2: "))
marks3 = int(input("Enter marks for Subject 3: "))

# Create an instance of the Student class
student1 = Student(name, marks1, marks2, marks3)

# Print the student's details and average marks
student1.print_details()

"""

# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

# Answer:

class Account:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance
        
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Debited {amount}. Remaining balance: {self.balance}")
    
    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance: {self.balance}")
    
    def print_balance(self):
        print(f"Account No: {self.account_no}, Balance: {self.balance}")

# Example usage
account1 = Account(account_no=12345, balance=500)
account1.print_balance()
account1.credit(200)
account1.debit(100)
# account1.debit(700)
