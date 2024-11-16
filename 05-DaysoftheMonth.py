## Exercise 5: Days of the Month - 30 Marks

# Write a program that tells a user how many days there are in a specific month.
# Use a dictionary to map the month numbers (1-12) to the number of days in each month.
## Instructions:
# 1. Create a Dictionary: Define a dictionary where the keys are month numbers and values are the number of days in those months.
# 2. Input Handaling: Ask the user to input the month number.
# 3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
## Advanced Requirement:
# Leap Year Adjustment: Modify the program to account for leap years. 
# For February, ask the user if the year is a leap year and adjust the number of days accordingly.

## Input

days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month = int(input("Enter the month number (1-12): "))
if 1 <= month <= 12:
    if month == 2:
        leap_year = input("Is it a leap year? (yes or no): ").strip().lower()
        if leap_year == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        print(f"The month has {days_in_month[month]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")

## Output

# Enter the month number (1-12): 1
# The month has 31 days.
# Enter the month number (1-12): 2
# Is it a leap year? (yes or no): yes
# February has 29 days in a leap year.
# Enter the month number (1-12): 2
# Is it a leap year? (yes or no): no
# February has 28 days.
# Enter the month number (1-12): 3
# The month has 31 days.
# Enter the month number (1-12): 4
# The month has 30 days.
# Enter the month number (1-12): 5
# The month has 31 days.
# Enter the month number (1-12): 6
# The month has 30 days.
# Enter the month number (1-12): 7
# The month has 31 days.
# Enter the month number (1-12): 8
# The month has 31 days.
# Enter the month number (1-12): 9
# The month has 30 days.
# Enter the month number (1-12): 10
# The month has 31 days.
# Enter the month number (1-12): 11
# The month has 30 days.
# Enter the month number (1-12): 12
# The month has 31 days.
# Enter the month number (1-12): 13
# Invalid month number. Please enter a number between 1 and 12.

## Description
# 1. Define Days in Each Month:
#    - We use a dictionary, 'days_in_month', where keys are month numbers (1-12) and values are days in each month.
# 2. User Input:
#    - The program asks the user to inout a month number between 1 and 12.
# 3. Validate Input:
#    - An 'if' statement checks if the month is within the valid range.
# 4. Leap Year Adjustment for February:
#    - If the month is '2' (February), the program asks the user if it's a leap year.
#    - If the user says 'yes', February has 29 days; otherwise, it has 28 days.
# 5. Display Days for Other Months:
#    - For other months, it directly uses the dictionary to display the number of days.
# 6. Handle Invalid Input:
#    - If the month is not between '1' and '12', it shows an error message.