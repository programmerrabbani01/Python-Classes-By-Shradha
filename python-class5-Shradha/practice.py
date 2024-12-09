
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

