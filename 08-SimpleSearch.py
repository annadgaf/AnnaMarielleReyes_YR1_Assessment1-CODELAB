## Exercise 8: Simple Search - 30 Marks

# Write a program that searches for a specific string within a list of strings. 
# The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). ,
# and your task is to search for "Sam".
## Optional Requirements:
# 1. Allow the user to input the search term instead of using a predefined value.
# 2. Implement the search functionality based on user input.

## Input

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave".]
search_term = input("Enter the name you want to search for: ")
if search_term.lower() in (name.lower() for name in names):
    print(f"{search_term} was found in the list!")
else: 
    print(f"{search_term} was not found in the list.")