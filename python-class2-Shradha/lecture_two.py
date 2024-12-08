
"""
# for make a line break next line

srt1 = "This is a string.\nWe make it in PYTHON";

# for make tab in a line

srt2 = "This is a string.\tWe make it in PYTHON";

print(srt1);
print(srt2);

"""
"""
# concatenation

first = "PROGRAMMER";
SECOND = "RABBANI"

concatenated = first + " " + SECOND;

print(concatenated);

# length

length = len(concatenated);

print(length);


# indexing

str = "Golam Rabbani"

ch = str[6]

print(ch);


# slicing

stri = "programmer rabbani"

# sliced = str[starting_index : ending_index]

# sliced = stri[5:12];  # from 5th to 12th index
sliced = stri[10:len(stri)];  # from 510th to last
# sliced1 = stri[:2];  # from 0 to 2 index
# sliced2 = stri[11:18];  # from 11th to 18th index

print(sliced);
# print(sliced1 + " " + sliced2);

# negative index

str1 = "RABBANI" # it's a negative index. it's count form last. like (-1 means I). it's not start with 0. it's start with -1

ch1 = str1[-7:-4];

print(ch1);

# replace

str = "DEVELOPER RABBANI"

replaced = str.replace("DEVELOPER","PROGRAMMER")

print(replaced)


# functions

# 1. endswith function

# with this function we can know is my string  ends with my last character which i want to print

str = "My Name Is Rabbani"

result = str.endswith("Rabbani");

print(result);

# 2. capitalize function

# with this function we can capitalize my string first character only

str = "my Name Is Rabbani"

capitalized = str.capitalize();

print(capitalized);

# 3. find function

# with this function we can find a particular character index form string, and also can find a character, if i want to find a character it's show me that character where it's defined first only

str = "My Name Is Rabbani"

# index = str.find("Is");
index = str.find("a");

print(index);

# 4. count function

# with this function we can count how many times a particular character in my string. and also can count full word

str = "My Name Is Rabbani"
str2 = "i love python and also love javascript"

count = str.count("a");
count2 = str2.count("love");

print(count);
print(count2);

"""

#################################################

# conditional statements (if-elif-else)

# age = int(input("Type your age: "))

# if age > 0 and age < 18:
#     print("You are a child")
# elif age >= 18:
#     print("You are an adult")
# else:
#     print("Invalid age")
    

# biyaAge = 15;

# if (biyaAge >= 18):
#     print("You can marriage");

# elif (biyaAge <= 18):
#     print("You are not eligible for marriage");

# else :
#     print("Invalid age");


# grade students based on marks

# marks = int(input("Enter your marks: "));

# if marks >=90:
#     # print("Grade A");
#     grade = "A"

# elif marks >=80 and marks < 90:
#     # print("Grade B");
#     grade = "B"

# elif marks >=70 and marks < 80:
#     # print("Grade C");
#     grade = "C"

# elif marks >=60 and marks < 70:
#     # print("Grade D");
#     grade = "D"

# else:
#     # print("Grade F");
#     grade = "F"
    
# print("Your Grade is -> ", grade);


# NESTING CODE

age = 18;

if age >= 20:
    if age >= 80:   
        print("You can't drive");
    else:
        print("You can drive ");

else:
    print("you can't drive");



