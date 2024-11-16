## Exercise 6: Brute Force Attack - 30 Marks

# Write a program that stimulates a password entry system. The correct passwords is defines as 12345.
# The program should keep asking the user to enter the password until they provide the correct one.
## Basic Requirements:
# 1. Define the correct password.
# 2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
# 3. Output an appropriate message when the correct password is entered.
## Optional Requirements:
# Modify the program to include a maximum of 5 password attempts. 
# If the user enters the wrong password, inform them of the remaining attempts. 
# If the maximum number of attempts is reached, inform the user that the authorities have been alerted.

## Input

correct_password = "12345"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    user_input = input("Enter the password: ")

    if user_input == correct_password:
        print("Access Granted!")
        break
    else: 
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Wrong password. You have {remaining_attempts} attempts left.")
        else: 
            print("Maximum attempts reached. U.A.E. authories have been alerted.")
            break

## Output

# Enter the password: 123123
# Wrong password. You have 4 attempts left.
# Enter the password: 213312
# Wrong password. You have 3 attempts left.
# Enter the password: 123123
# Wrong password. You have 2 attempts left.
# Enter the password: 1231
# Wrong password. You have 1 attempts left.
# Enter the password: 2131
# Maximum attempts reached. U.A.E. authories have been alerted.

## Description
# 1. Defining the Correct Password and Maximum Attempts
# - 'correct_password' as the passwords the user must input to gain access.
# - 'max_attempts' to limit the number of the times a user can try entering the password.
# 2. Initializing the Counter
# We need a counter to track how many times the user has tried entering a password.
# We initialize it as 0
# 3. Using a while Loop
# We use a 'while' loop to repeat the process of asking the user for the password until one of two things happens:
# - The user enters the correct password; or
# - The user reaches the maximum number of attempts.
# 4. Asking for the Password
# Inside the loop, we ask the user to input the password.
# 5. Checking the Password
# Once the user inputs a password, we check:
# - If the password is correct:
#   - If it matched 'correct_password', we print an access message and exit the loop using break.
# - If the passwords is incorrect:
#   - We inceremnt the 'attempts' counter by 1.
#   - Then, we calculate how many attempts are left using:
# 'remaining_attempts = max_attempts - attempts'
#   - We inform the user how many attempts are left. If no attempts remain, we print a final message
#     indicating authorities have been alerted.
