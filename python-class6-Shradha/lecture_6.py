# Functions in Python

"""
    
def age_cal(current_year, birth_year):
    age = current_year - birth_year
    return age

# Example usage
current_year = 2024
birth_year = int(input("Enter Your Birth Year :"))

age = age_cal(current_year, birth_year)
print(f"Your age is: {age}")

"""

# average of 3 numbers

"""

def avgNum (a,b,c):
    avg = (a + b + c) / 3
    return avg

# Example usage

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

average = avgNum(a, b, c)

print(f"The average of {a}, {b}, and {c} is: {average}")

"""



# print("Golam Rabbani", end=" ") # end = " " use for same line
# print("The Programmer")


# Recursion

"""  
def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)

show(5)

def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
    print("End")

show(3)

# Recursion factorial

n = 4
def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        result = n * fact(n - 1)
        print(f"factorial({n}) returns {n} * factorial({n - 1}) = {result}")
        return result
    
print(f"Factorial of {n} is: {fact(n)}")
"""



