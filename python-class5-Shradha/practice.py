
# while loop

# Print numbers from 1 to 100.

# Answer:

"""
i = 1;

while i <= 100:
    print(f"{i} : Hello World! ")
    i += 1
"""

# Print numbers from 100 to 1.

# Answer:
"""
i = 100;

while i >= 1:
    print(f"{i} : Hello World! ")
    i -= 1
"""

# Print the multiplication table of a number n.

# Answer:

""" 
n = int(input("Enter the number :"))

i = 1;

while i <= 10:
    print(f"{n*i} : Hello World! ")
    i += 1
"""

# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# Answer:
"""
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

i = 0;

while i < len(nums):
    print(f"{nums[i]} : Hello World! ")
    i += 1
    
"""

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# Answer:

"""


#for loop
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = int(input("Enter the number to search :"))

found = False

i = 0;

while i < len(nums) and not found:
    if nums[i] == x:
        found = True
    else:
        i += 1

if found:
    print(f"{x} found in the tuple at index!",i)
else:
    print(f"{x} not found in the tuple!")

"""


# for loop

# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# Answer:
"""
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for num in nums:
    print(f"{num} : Hello World! ")
    
"""

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# Answer:
"""
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = int(input("Enter the number to search :"))

i = 0;

for num in nums:
    if num == x:
        print(f"{x} is found in the tuple at index.",i)
        break;
    i += 1
else:
    print(f"{x} is not found in the tuple.")
    
"""

# range check

# using for & range()
# Print numbers from 1 to 100.
# Print numbers from 100 to 1.
# Print the multiplication table of a number n.

# Answer:
"""
for i in range(1,101):
    print(f"{i} : Hello World! ")
"""  
"""
for i in range(100, 0 , -1): # 101 start, 0 end and -1 decrease
    print(f"{i} : Hello World! ")
"""
"""
n = int(input("Enter a number :"))

for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")
"""

# WAP to find the sum of first n numbers. (using while)

# Answer:

"""
n = int(input("Enter the number of terms : "))
sum = 0

for i in range(1, n+1):
    sum += i

print(f"The sum of first {n} numbers is {sum}")

"""
"""
n = int(input("Enter the number of terms: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f"The sum of the first {n} numbers is {sum}")

"""

# WAP to find the factorial of first n numbers. (using for)

# Answer:

n = int(input("Enter the number of terms: "))

print(f"Factorials of the first {n} numbers:")
for num in range(1, n + 1):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
