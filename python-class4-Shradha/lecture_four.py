# Dictionary in Python

""" 
import json;

info = {
    "name":"Rabbani",
    "email":"rabbani@gmail.com",
    "age": 25,
    "hobbies": ["reading", "painting", "coding"],
    "grades": [85, 90, 92],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    },
    "topics":("Dictionary", "Sets"),
    "isStudent": True,
}

# change Value
info["email"] = "rabbani@yahoo.com"
# add new value
info["sureName"] = "Faisal"

# print(info["address"])
# print(info["name"])

# print(json.dumps(info, indent= 4))

print(info)

null_dic = {}

null_dic["name"] = "Rabbani"

print(null_dic)

"""

# Nested Dictionaries

"""
student = {
    "name": "John Doe",
    "age": 20,
    "grade": 95,
    "subjects": {
        "Math": 85,
        "English": 90,
        "Science": 92
    }
}

student["subjects"]["Math"] = 95

print(student["subjects"])
# print(student["subjects"]["Math"])

"""

# Dictionary Methods

"""
student = {
    "name": "John Doe",
    "age": 20,
    "grade": 95,
    "subjects": {
        "Math": 85,
        "English": 90,
        "Science": 92
    }
}

# keys() method

print(student.keys());

# type casting for converting to normal list

print(list(student.keys()));
print(len(list(student.keys())));

# values() method
print(student.values());
print(list(student.values()));

# items() method. return tuple
print(student.items());
print(list(student.items()));

# catch single value from list
pairs = list(student.items());
print(pairs[0])

# get() method

print(student["name"])
print(student.get("name"))


# update() method

newVal = {"email":"jasmin@example.com"};
newVal2 = {"name":"Jasmin Smith"}
student.update(newVal);
student.update(newVal2);

print(student);
"""

# Set in Python

"""
collection = {1,2,3,4,1,2,3,4,"Hello", "world","world"}

# set ignore duplicate values
print(collection)
print(type(collection))
print(len(collection))

collection2 = set()

collection2.add(1)
collection2.add(2)
print(collection2)
print(type(collection2))

"""

# Set Methods

"""
# add() method


collection = {1,2,3,4,5}
collection.add(6)
collection.remove(5)
print(collection)

# union() method

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}

union_set = set1.union(set2)

print(set1)
print(set2)
print(union_set)

# intersection() method

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}

intersection_set = set1.intersection(set2);

print(set1);
print(set2);
print(intersection_set);

"""




