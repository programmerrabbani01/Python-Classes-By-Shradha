"""

import json

students = [
    {
        "name": "Alice",
        "grade": 95,
        "subjects": ["Math", "Science", "English"],
        "attendance": 90,
        "grade_percentage": 95
    },
    {
        "name": "Bob",
        "grade": 85,
        "subjects": ["Math", "Science", "History"],
        "attendance": 85,  
        "grade_percentage": 85
    },
    {
        "name": "Charlie",
        "grade": 90,
        "subjects": ["Math", "English", "Geography"],
        "attendance": 95,
        "grade_percentage": 90
    }
]

# print(students)
print(json.dumps(students, indent=4))

print(students.name[1:4])

student = ["Rabbani", 27, "Patuakhali"]

student[0] = "Faisal"
student[1] = 30
student[2] = "Dhaka"

print(student)
print(len(student))

# slicing
marks = [20,30,40,50,60,80]

print(marks[1:])
print(marks[1:3])
print(marks[:3])
print(marks[-3:-1])



# list methods

students = ["Charlie","Bob","Alice"]
marks = [1,2,3]
foods = ["Potato","Law", "Tomato","Orange"]
points = [20,30,40,50,60,80]
rMarks = [1,2,3,4,5,3,4,5]
pMarks = [1,2,3,4,5,3,4,5]

students.append("Robort")
students.sort()

marks.append(4)
marks.sort(reverse=True)
foods.reverse()
points.insert(0,10)
points.insert(6,70)
rMarks.remove(3)
pMarks.pop(4)


print(students)
print(marks)
print(foods)
print(points)
print(rMarks)
print(pMarks)

tup = (1,2,3,1)

print(tup.count(1))
# find index number
print(tup.index(2))

"""



