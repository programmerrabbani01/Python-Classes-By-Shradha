# loops 

# while loops

"""

# count = 1;

# while count <= 5:
#     print(f"{count}: Hello")
#     count += 1

# print("Loop Ended")

# i = 1;

# while i <= 10:
#     print(f"{i} : World");
#     i += 1

# print("Loop Ended")

# i = 100;

# while i >= 50:
#     if i == 55:
#         break;
#     print(f"{i} : World");
#     i -= 1


# print("Loop Ended")

# i = 100

# while i >= 50:
#     if i == 55:
#         print(f"{i} : Love")
#         break
#     if i == 65:
#         print(f"{i} : Python")
#     if i == 85:
#         print(f"{i} : Programming")
    
#     print(f"{i} : World")
#     i -= 1

# print("Loop Ended")

# Break & Continue

# Break

# i = 100

# while i >= 50:
#     if i == 55:
#         print(f"{i} : Love")
#         break
    
#     print(f"{i} : World")
#     i -= 1

# print("Loop Ended")

# Continue

# i = 0

# while i <= 10:
#     if i == 3:
#         i += 1
#         continue
    
#     print(f"{i} : World")
#     i += 1

# print("Loop Ended")

# find odd skip even
# i = 1

# while i <= 10:
#     if i%2 == 0:
#         i += 1
#         continue #skip
    
#     print(f"{i} : World")
#     i += 1

# print("Loop Ended")

# find even skip odd

# i = 1

# while i <= 10:
#     if i%2 != 0:
#         i += 1
#         continue #skip
    
#     print(f"{i} : World")
#     i += 1

# print("Loop Ended")
"""

# For loop
"""
list = [1,2,3,4,5]

for items in list:
    if items == 3:
        print("3 found")
        break;
    print(items)
else:
    print("Loop Ended")
    


import json;

devs = [
    {
        "id":"1",
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    },{
        "id":"2",
        "name": "Jane Doe",
        "age": 28,
        "city": "Los Angeles"
    },{
        "id":"3",
        "name": "Alice Doe",
        "age": 32,
        "city": "Chicago"  
    },{
        "id":"4",
        "name": "Bob Doe",
        "age": 29,
        "city": "San Francisco"
    },{
        "id":"5",
        "name": "Charlie Doe",
        "age": 31,
        "city": "New York"
    }
]

for dev in devs:
        print(json.dumps(dev, indent=4))
        
        
"""

# range
"""
for i in range(11):
    print(f"{i} : End Range Only")

print("Loop Ended")

for i in range(1, 11):
    print(f"{i} : Start & End Range")

print("Loop Ended")

for i in range(1, 11, 2):
    print(f"{i} : Start , End & increase  Range")

print("Loop Ended")
"""

# pass Statement
"""
for i in range(10):
    pass

print("Work later")
"""