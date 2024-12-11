# File I/O in Python 

""" 
1.Text Files : .txt, .docx, .log etc.
2. Binary Files : .mp4, .mov, .png, .jpeg etc. 

"""

# Open, read & close File

"""
f = open("demo.txt","r")
data = f.read()

print(data)

f.close()

"""

# Reading a file

"""
f = open("demo.txt","r")

# data = f.read(20)
line = f.readline()
line2 = f.readline()

print(line)
print(line2)

f.close()

"""
# Writing to a file

"""
f = open("demo.txt", "w")

data = f.write("i love javascript")

f.close()

"""

# add a new text to a file

"""
# Open the file in append+ mode (write and read)
f = open("demo.txt", "a+")

# Append a new line to the file
f.write("\ni love javascript")

# Move the cursor to the beginning of the file
f.seek(0)

# Read the content of the file
data = f.read()

# Close the file
f.close()

# Print the content
print(data)

"""

# create a new file like sample.txt

"""
# f = open("sample.txt", "w")

# or

# f = open("sample.txt", "x")  # create a new file

# or

f = open("sample.txt", "a")  # create a new file

f.close()

f = open("sample.txt", "r+")

f.write("Hello bro ")

print(f.read())


f.close()
"""

# with Syntax
"""
with open("sample.txt", "r") as f:
    data = f.read()
    
    print(data)

with open("sample.txt", "w") as f:
    f.write("New Data Added ")
    
    print(data)

with open("sample.txt", "a") as f:
    f.write("Successful !")
    
    print(data)
"""

# Deleting a File
"""
import os

# Remove the file

os.remove("sample.txt")
"""