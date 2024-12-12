# Class & Object in Python

""" 
class Students:
    name = "Rabbani"
    email = "rabbani@gmail.com"
    age = 27
    
s1 = Students()

print(s1.name, s1.email, s1.age)

"""

# _ _init_ _ Function

# 1st method
"""
class Student:
    
    # default constructor
    def __init__(self):
        pass
    
    college_name = "PTK. GOVT. COLLEGE"
    school_name = "PTK. GOVT. JUBILEE HIGH SCHOOL"
    
    # parameter constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        print("adding new student in database . . . .")
        
s1 = Student("G M GOLAM RABBANI","rab@gmail.com", 27)
s2 = Student("Faisal","faigmail.com", 24)
s3 = Student("Omor Farukh","omorfarukh@gmail.com", 2.5)

print(f"Your name is : {s1.name}, your email is : {s1.email}, your age is : {s1.age} and your college is : {s1.college_name}.")

print(f"Your name is : {s2.name}, your email is : {s2.email}, your age is : {s2.age} and your college is : {s2.college_name}.")

print(f"Your name is : {s3.name}, your email is : {s3.email}, your age is : {s3.age} and your college is : {s3.school_name}.")
"""

# 2nd method json object

""" 
import json

class Student:
    # Default and parameterized constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        print("Adding new student in database . . . .")

    # Function to return student data as a dictionary
    def to_dict(self, school_or_college):
        return {
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "institution": school_or_college
        }

# Static attributes for institutions
Student.college_name = "PTK. GOVT. COLLEGE"
Student.school_name = "PTK. GOVT. JUBILEE HIGH SCHOOL"

# Creating student instances
s1 = Student("G M GOLAM RABBANI", "rab@gmail.com", 27)
s2 = Student("Faisal", "faigmail.com", 24)
s3 = Student("Omor Farukh", "omorfarukh@gmail.com", 2.5)

# Creating JSON strings for each student
s1_json = json.dumps(s1.to_dict(Student.college_name), indent=4)
s2_json = json.dumps(s2.to_dict(Student.college_name), indent=4)
s3_json = json.dumps(s3.to_dict(Student.school_name), indent=4)

# Printing JSON strings
print(s1_json)
print(s2_json)
print(s3_json)

"""

# 3rd method using __slots__

"""


import json

class Student:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        print("Adding new student in database . . . .")

    # Function to return student data as a dictionary
    def to_dict(self, school_or_college):
        return {
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "institution": school_or_college
        }

# Static attributes for institutions
Student.college_name = "PTK. GOVT. COLLEGE"
Student.school_name = "PTK. GOVT. JUBILEE HIGH SCHOOL"

# Creating student instances
s1 = Student("G M GOLAM RABBANI", "rab@gmail.com", 27)
s2 = Student("Faisal", "faigmail.com", 24)
s3 = Student("Omor Farukh", "omorfarukh@gmail.com", 2.5)

# Collecting all students in a list of dictionaries
students_data = [
    s1.to_dict(Student.college_name),
    s2.to_dict(Student.college_name),
    s3.to_dict(Student.school_name)
]

# Converting the list to a JSON string
students_json = json.dumps(students_data, indent=4)

# Printing the JSON string
print(students_json)

"""

# Methods

"""
class Student:
    college_name = "PTK. GOVT. COLLEGE"
    school_name = "PTK. GOVT. JUBILEE HIGH SCHOOL"

    # Parameterized constructor
    def __init__(self, name, email, age, institution_type="college"):
        self.name = name
        self.email = email
        self.age = age
        self.institution_type = institution_type

    def get_institution(self):
        return self.college_name if self.institution_type == "college" else self.school_name

    def welcome(self):
        institution = self.get_institution()
        return f"Hello, my name is {self.name}, my email is: {self.email}, my age is: {self.age} and I am from {institution}."

# Creating student instances
s1 = Student("G M GOLAM RABBANI", "rab@gmail.com", 27, "college")
print(s1.welcome())
s2 = Student("Faisal", "faigmail.com", 24, "college")
print(s2.welcome())
s3 = Student("Omor Farukh", "omorfarukh@gmail.com", 2.5, "school")
print(s3.welcome())

"""

# Static Methods

"""
class Student:
    @staticmethod
    def college():
        return "PTK. GOVT. COLLEGE"
    print(college())
    
"""


# Abstraction

"""
class Car:
    
    def __init__(self):
        self.accelerator = False
        self.brake = False
        self.clutch = False
    
    def start(self):
        self.accelerator = True
        self.clutch = True
        print("Car started...")
    
    def stop(self):
        self.accelerator = False
        self.brake = True
        self.clutch = False
        print("Car stopped...")

car1 = Car()
car1.start()
car1.stop()

"""