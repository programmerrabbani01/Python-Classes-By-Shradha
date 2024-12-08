"""
Store following word meanings in a python dictionary :

table : “a piece of furniture”,“list of facts & figures”

cat : “a small animal”

# Answer
new_dict = {
    "table": ["a piece of furniture","list of facts & figures"],
    "cat": "a small animal"
}

print(new_dict)
"""

"""
You are given a list of subjects for students. Assume one classroom is required for 1 . How many classrooms are needed by all students.

”python”,“java”,“C++”,“python”,“javascript”,

“java”,“python”,“java”,“C++”,“C”

# Answer

students = {
    "python","java","C++","python","javascript",
    "java","python","java","C++","C"
    }

classrooms = len(students)

print(classrooms)

"""

"""
WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value.


# Answer

marks ={}

# marks["Math"] = int(input("Enter Math marks: "))
# marks["English"] = int(input("Enter English marks: "))
# marks["Bangla"] = int(input("Enter Bangla marks: "))

math = int(input("Enter Math marks: "))
marks.update({"Math": math})
eng = int(input("Enter English marks: "))
marks.update({"English": eng})
bng = int(input("Enter Bangla marks: "))
marks.update({"Bangla": bng})

print(marks)

"""

"""

Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)

"""

# Answer

values = {
    ("int", 9),
    ("float", 9.0)
}

print(values);
