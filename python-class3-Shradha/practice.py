# WAP to ask the user to enter names of their 3 favorite movies and store them in a list

""" 
movies = []
# mov1 = input("Enter 1st Movie Name :")
# mov2 = input("Enter 2nd Movie Name :")
# mov3 = input("Enter 3rd Movie Name :")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

mov = input("Enter 1st Movie Name :")
movies.append(mov)
mov = input("Enter 2nd Movie Name :")
movies.append(mov)
mov = input("Enter 3rd Movie Name :")
movies.append(mov)

movies.append(input("Enter 1st Movie Name :"));

movies.append(input("Enter 2nd Movie Name :"));

movies.append(input("Enter 3rd Movie Name :"));




print(movies) # Printing the list of favorite movies entered by the user.

"""

# WAP to check if a list contains a palindrome of elements . (Hint : use copy() method)

"""
list = [1,2,3]
list1 = [1,2,1]

copy_list = list.copy()
copy_list.reverse()

copy_list1 = list1.copy()
copy_list1.reverse()

str = ["m","a","a","m"]
str1 = ["m","a","a","m","s"]

str = str.copy()
str.reverse()

str1 = str1.copy()
str1.reverse()

if copy_list == list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

if copy_list1 == list1:
    print("The list1 is a palindrome.")
else:
    print("The list1 is not a palindrome.")

if str == str:
    print("The str is a palindrome.")
else:
    print("The str is not a palindrome.")

if str1 == str1:
    print("The Str1 is a palindrome.")
else:
    print("The Str1 is not a palindrome.")
    
""" 

# WAP to count the number of students with the "A" grade in the following tuple.

grade = ("D", "B", "C", "D", "A", "B", "A", "D", "A")

print(grade.count("A"))

# Then store the above values  in a list and sort them form "A" to "D"

grade1 = ["D", "B", "C", "D", "A", "B", "A", "D", "A"]

grade1.sort()

print(grade1)