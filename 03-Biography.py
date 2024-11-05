## Exercise 3: Biography - 25 Marks

# In this exercise, you'll create a prgram that stores and prints your name, hometown, and age to the console using a Python dictionary.
## Steps:
# 1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
# 2. Print the values on separate lines using a single 'print()' statement.
# 3. Use variables with appropriate data types for each pieve of information.
## Advanced Requirements:
# Have the user input their name, hometown, and age instead of hardcoding the values.
# Try giving both your first and second name when asked for your name.
# What happens? How can you handle multiple words in Python?
# Test the program by entering a string value for age (e.g., "twenty").
# What happens? How can you prevent this issue?

## Input

name = input("Enter your name (First and last name): ")
hometown = input("Enter your hometown: ")
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age) 
        break 
    else:
        print("Please enter an integer for your age.")
print(f"Name: {name}\nHometown: {hometown}\nAge: {age}")

## Output

# Enter your name (First and last name): Anna Marielle Reyes
# Enter your hometown: Bulacan, Philippines
# Enter your age: Eighteen
# Please enter an integer for your age.
# Enter your age: 18
# Name: Anna Marielle Reyes
# Hometown: Bulacan, Philippines
# Age: 18

## Description:
# 1. Ask for Name: The program starts by asking the user to enter their name,
# including their first and last names. This information is saved in a variable called 'name'.
# 2. Ask for Hometown: Next, it asks the user for their hometown and saves this information
# in a variable called 'hometown'.
# 3. Get Age with Checks: The program then enters a loop to get the user's age:
#    - It asks the user to enter their age and saves it in a variable called 'age'.
#    - The code checks if the age is a number using the 'isdigit()' method. 
#      This checks if the input only has digits.
#    - If the input is a number, it changes 'age' from a string to an integer and stops the loop.
#    - If the input is not a number, it tells the user to enter a number for their age,
#      and the loop continues, asking for the age again.
# 4. Show the Information: Finally, after getting a valid age, the program prints the user's name,
# hometown, and age on separate lines.
# This code collects user information and makes sure the age is an integer before showing the results.