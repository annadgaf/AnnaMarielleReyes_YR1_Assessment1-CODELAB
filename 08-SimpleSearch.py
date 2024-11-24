## Exercise 8: Simple Search - 30 Marks

# Write a program that searches for a specific string within a list of strings. 
# The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). ,
# and your task is to search for "Sam".
## Optional Requirements:
# 1. Allow the user to input the search term instead of using a predefined value.
# 2. Implement the search functionality based on user input.

## Input

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_term = input("Enter the name you want to search for: ")
if search_term.lower() in (name.lower() for name in names):
    print(f"{search_term} was found in the list!")
else: 
    print(f"{search_term} was not found in the list.")

## Output
# Enter the name you want to search for: Jake
# Jake was found in the list!
# Enter the name you want to search for: zac
# zac was found in the list!
# Enter the name you want to search for: IAN
# IAN was found in the list!
# Enter the name you want to search for: RoN
# RoN was found in the list!
# Enter the name you want to search for: Anna
# Anna was not found in the list.

# Description
# 1. List of Names:
# - The program begins with a predefined list of names.
# 2. Getting User Input:
# - The program asks the user to type the name they want to find.
# - For example, the user might type "jake", "JAKE", or "JaKe".
# 3. Case-Insensitive Search:
# - Programs usually treat "Jake" and "jake" as different because they consider 
# uppercase and lowercase letters as distinct.
# - To fix this, the program converts both the user's input and names in the list 
# to lowercase, making the search ignore capitalization.
# - This is done with the .lower() function that I learned from sololearn.
# 4. Checking if the Name is in the List:
# - The program creates a new list where all names are in lowercase.
# - It then checks if the lowercase version of the user's input matches any name in this new list.
# 5. Output:
# - If the name is found, the program will say: "<name> was found in the list!".
# - If the name is not found, it will say: "<name> was not found in the list.".