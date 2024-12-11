# Functions in Python


# WAF to print the length of a list. ( list is the parameter)

#  Answer:

""" 
my_list = [1, 2, 3, 4, 5]

def print_list_length(list):
    print(len(list))


print_list_length(my_list)  # Output: 5
"""

# WAF to print the elements of a list in a single line. ( list is the parameter)

# Answer:

"""
# 1st method

my_list = [1, 2, 3, 4, 5]

def print_list_elements(list):
    print(*list)  # Output: 1 2 3 4 5

print_list_elements(my_list)

# 2nd method

list = [1, 2, 3, 4, 5]
def printList (list):
    for item in list:
        print(item,end=" ")
        
printList(list)
"""

# WAF to find the factorial of n. (n is the parameter)

# Answer:

"""
n = 5

def factorial(n):
    if n == 0:
        print(f"factorial({n}) returns 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"factorial({n}) returns {n} * factorial({n - 1}) = {result}")
        return result

print(f"Factorial of {n} is: {factorial(n)}")
"""

# WAF to convert USD to INR.

# Answer:

"""

def usd_to_bdt(usd_amount, conversion_rate=119.00):
    bdt_amount = usd_amount * conversion_rate
    return bdt_amount

# Example usage
usd_amount = int(input("Type your amount :"))
conversion_rate = 119.00  # Example conversion rate, you should update this with the latest rate

bdt_amount = usd_to_bdt(usd_amount, conversion_rate)
print(f"${usd_amount} USD is equal to Tk{bdt_amount} BDT")

"""

"""
def oddOrEven(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
number = int(input("Type the number :"))
result = oddOrEven(number)
print(f"{number} is {result}")

"""

# Recursion &  Recursion factorial

# Write a recursive function to calculate the sum of first n natural numbers.

# Answer:

"""

def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)
    
sum = sum_of_natural_numbers(5) # the sum come from 1 to 5. like (1+2+3+4+5)

print(sum)

"""

# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

# Answer:



def print_list_elements(list, index=0):
    if index >= len(list):
        return
    else:
        print(list[index])
        print_list_elements(list, index + 1)

my_list = ["Alo", "Potol", "Law", "Kumra", "Tomato"]
print_list_elements(my_list)

