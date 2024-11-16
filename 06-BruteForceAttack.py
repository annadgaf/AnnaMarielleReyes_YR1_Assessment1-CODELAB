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

