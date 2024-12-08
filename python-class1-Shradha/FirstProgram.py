# print("Hello, world!")
# print("G M Golam","Rabbani")
# print("Hello, world!\nG M Golam Rabbani")

# from typing import List

# name: str = "Rabbani"
# age: int = 29
# skills: List[str] = ["Python", "JavaScript"]

# print(f"Name: {name}, Age: {age}, Skills: {skills}")

# user_info = {
#     "name": "Rabbani",
#     "age": 29,
#     "skills": ["Python", "JavaScript"]
# }

# print(user_info)

########################################################################

# name = "Rabbani"
# age = 29
# skills = ["Python", "JavaScript"]

# print("my name is    :", name)
# print("my age is     :", age)
# print("my skills are :", skills)

# # Proper string formatting using f-strings
# print(f"Hi! My Name Is {name}, I'm {age} Years Old, and My skills Are {', '.join(skills)}")


# name = "Rabbani"
# age = 25
# skills = ["javascript", "python"]
# isMarried = True
# job = None

# print(type(name))
# print(type(age))
# print(type(skills))
# print(type(isMarried))
# print(type(job))


########################################################################

# 1st method

# title = "IPhone 16 Pro"
# price = 1299.99
# Formatting the price with currency symbol and two decimal places
# formatted_price = f"${price:.0f}"
# formatted_price = f"${price:.1f}"
# formatted_price = f"${price:.2f}"
# formatted_price = f"${price:.3f}"

# Using f-string to concatenate the title and formatted price
# print(f"{title} - {formatted_price}")

# print(f"This Is {title} And It's Price is {formatted_price}")

# 2nd method

# title = "IPhone 16 Pro"
# price = 1299.99

# Round the price to the nearest whole number
# rounded_price = round(price)

# Using f-string to concatenate the title and rounded price
# formatted_price = f"${rounded_price}"

# print(f"{title} - {formatted_price}")
# print(f"This Is {title} And Its Price is {formatted_price}")

########################################################################

# Assignment operator

# age = 25

# age2= age

# print(age2)

########################################################################

# Types of Operators


# Arithmetic Operators

# a= 5
# b= 2

# sum = a + b

# print(sum)

"""
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b) a^b

"""

# relational / comparison operators

"""
a= 5
b= 2

print(a == b)  # False
print(a!= b)  # True
print(a > b)  # True -> b er theke a boro kin na tar jonno (>) sign
print(a < b)  # False -> a er theke b boro kin na tar jonno (<) sign
print(a >= b)  # True -> b er theke a boro kin na tar jonno (>=) sign
print(a <= b)  # False -> a er theke b boro kin na tar jonno (<=) sign

"""

# assignment operators

"""
num= 10

num += 5  # num = num + 5
num -= 5  # num = num - 5
num *= 2  # num = num * 2
num **= 2  # num = num ** 2
num /= 2  # num = num / 2
num //= 2  # num = num // 2
num %= 2  # num = num % 2

print(num)
"""

# logical operators

"""
a= 50
b= 30

print(not (a > b))  # er mane hocce a b er theke boro na , jar karone ans Asbe False, karon a to b er theke boro
print(not (a < b))  # er mane hocce a b er theke boro , jar karone ans Asbe True, karon a to b er theke boro

c = False
d = True

print("and operator :", c and d) # jodi c abong d er value same hoi tahole true, r na hole false

print("or operator :", c or d) # jodi c othoba d er konota true hoi tahole true, r jodi donota value e Fasle hoi tahole false

print("or operator :", (a==b) or (a>b)) # ekhane (a==b) false and (a>b) true , jkhn tru ace tkhn total ans asbe true
"""

# type conversion

"""
# a = 2
# b = 4.25

# sum = a + b

# sum = int(b) + a  # float to int

# a = "2"
# b = 4.25

# a = int("2")
# a = float("2")
# b = 4.25

# sum = a + b

# type casting

# sum = float(a) + b  # string to float

print(sum)


a = 3.14

a = str(a)

print(type(a))

"""

# Input in

"""
name = input("Enter your name: ")

print("Hello, " + name)

age = int(input("Enter your age: "))    

print("Your Age Is :",  age)

"""

# price = float(input("Price: "))

# print("Your Price Is :", price)

"""
# 1st method

 formatted_price = f"${price:.0f}"

 print(f"Formatted Price: {formatted_price}")
"""
"""
# 2nd method

rounded_price = round(price)

print(f"Rounded Price: {rounded_price}")
"""


name = str(input("Your Name Is: "))
age = int(input("You Are: "))
marks = float(input("Your Marks Is: "))

# print(f"Name: {name}, Age: {age}, Marks: {marks}")

print("Your Name Is: ", name)
print("You Are: ", age, "years Old")
print("Your marks Are: ", marks)
