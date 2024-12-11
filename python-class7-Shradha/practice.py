# Create a new file “practice.txt” using python. Add the following data in it:

"""
Hi everyone
we are learning File I/O
using Java.
I lik programming in Java.

# Answer:

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI lik programming in Java.")
"""

# WAF that replace all occurrences of “java” with “python” in above file.

"""
# Answer:

with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("Java" ,"Python")

with open("practice.txt","w") as f:
    f.write(new_data)
print(new_data)

"""

# Search if the word “learning” exists in the file or not.

# Answer:

"""
# 1st method

with open("practice.txt","r") as f:
    data = f.read()
    
if "learning" in data:
    print("The word 'learning' exists in the file.")
else:
    print("The word 'learning' does not exist in the file.")
    
# 2nd method

word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    
    if (data.find(word) != -1):
        print("The word 'learning' exists in the file.")
    else:
        print("The word 'learning' does not exist in the file.")
        
# 3rd method


def check_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
    
        if (data.find(word) != -1):
            print("The word 'learning' exists in the file.")
        else:
            print("The word 'learning' does not exist in the file.")
            
check_word()

"""

# WAF to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.

# Answer:

"""
def check_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(f"The word 'learning' occurs in line {line_no}.")
                return
            line_no += 1
        
        return -1

print(check_line())

"""

# From a file containing numbers separated by comma, print the count of even numbers.

# Answer:


def count_even_numbers():
    count = 0
    with open("numbers.txt","r") as f:
        data = f.read()
        numbers = data.split(",")
        
        for num in numbers:
            if int(num) % 2 == 0:
                count += 1
    
    print(f"The count of even numbers is {count}.")

count_even_numbers()
