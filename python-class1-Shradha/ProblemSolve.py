"""
multi-line Comments

"""
# single Comments

"""
a= 1200
b= 600

sum = a + b
print(sum)

"""

# Write a Program to input 2 numbers & print their sum.

"""
first = input("Enter First Number:")
second = input("Enter Second Number:")

sum = int(first) + int(second)

print("Total Numbers Are :",sum)

"""


# WAP to input side of a square & print its area.

"""

side = input("Enter Side of Square:")

# area = int(side) * int(side)
area = int(side) ** 2

print("Area of Square is :",area)

"""

# WAP to input 2 floating point numbers & print their average.

"""

# a = input("Enter First Number:")
# b = input("Enter Second Number:")

a = float(input("Enter First Number:"))
b = float(input("Enter Second Number:"))

# average = (float(a) + float(b)) / 2

# print("Average of Two Numbers is :",average)
print("Average of Two Numbers is :", (a+b)/2)

"""

# WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False.



a = int(input("Enter A Number:"))
b = int(input("Enter B Number:"))

if a >= b:
    print("True")
else:
    print("False")