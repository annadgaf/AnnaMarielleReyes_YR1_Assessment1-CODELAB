# Assessment 1 Code lab Module by Anna Marielle Calangian Reyes
This repository is created by Anna Marielle Reyes and it contains a series of exercises given by the tutor and done by the student. Basic Python Exercises are given throughout this repository such as if-else exercises, python loops, arithmetic sequences, functions etc. These exercises are used to further improve coding knowledge and to show how to further elaborate and improve a code. In some exercises, multiple programs are given emphasising the difference between the normal program and an advanced program. These exercises are based on real-life situations which may be useful in the near future.


# List of Exercises
  - Exercise #1: Coding is Cool (01Codingiscool.py)
  - Exercise #2: Simple Sums (02SimpleSums.py)
  - Exercise #3: Biography (03Biography.py)
  - Exercise #4: Primitive Quiz (04.PrimitiveQuiz.py)
  - Exercise #5: Days Of The Month (05.DaysOfTheMonth.py)
  - Exercise #6: Brute Force Attack (06.BruteForceAttack)
  - Exercise #7: Some Counting (07.SomeCounting.py)
  - Exercise #8: Simple Search (08.SimpleSearch.py)
  - Exercise #9: Hello (09.Hello.py)
  - Exercise #10: Is it Even (10.IsItEven.py)


# Assessment 1 Code lab Module by Achilles Ratuiste Maling
This repository contains a series of exercises given by the tutor and done by the student. Basic Python Exercises are given throughout this repository such as if-else exercises, python loops, arithmetic sequences, functions etc. These exercises are used to improve coding knowledge and to show how to further elaborate and improve a code. In some exercises, multiple programs are given emphasising the difference between the normal program and an advanced program. These exercises are based on real-life situations in which may be useful in the near future.


# List of Exercises
  - Exercise #1: Coding is Cool (01Codingiscool.py)
  - Exercise #2: Simple Sums (02SimpleSums.py)
  - Exercise #3: Biography (03Biography.py)
  - Exercise #4: Primitive Quiz (04.PrimitiveQuiz.py)
  - Exercise #5: Days Of The Month (05.DaysOfTheMonth.py)
  - Exercise #6: Brute Force Attack (06.BruteForceAttack)
  - Exercise #7: Some Counting (07.SomeCounting.py)
  - Exercise #8: Simple Search (08.SimpleSearch.py)
  - Exercise #9: Hello (09.Hello.py)
  - Exercise #10: Is it Even (10.IsItEven.py)


## Exercise 1: Coding is Cool- 10 Marks


Fill in the blanks in the Python code below to output the phrase **"Coding is Cool"** to the console using variables and string concatenation.


### Result:
```python
#input 


word1 = "Coding "
word2 = "is "
word3 = "Cool"
print(word1 + word2 + word3)


## Output


# Coding is Cool


## Description:
# This code assigns "Coding " to word1, "is " to word2, and "Cool" to word3.
# It then combines these variables using the + operators and outputs the resulting string to the terminal.




```


__________________________________________________________________________________


## Exercise 2: Simple Sums - 15 Marks


In this exercise, you will create and work with integer variables, perform arithmetic operations, and print the result to the console.


### Steps:
1. Declare a variable and initialize it with the integer value `8`.
2. Declare a second variable and initialize it with the integer value `10`.
3. Declare a third variable that stores the sum of first two numbers.
4. Print the value of the sum to the console.


### Result:
```python
#input


int1 = 8
int2 = 10
sum = (int1 + int2)
print(sum)


## Output


# 18


## Description:
# This code starts by defining two integers: 
# int1 is set to 8 and int2 is set to 10. 
# It then adds these two integers together and saves the result in a variable called sum.
# Finally, it prints the value of sum to the screen, which is 18.




```


__________________________________________________________________________________


## Exercise 3: Biography - 25 Marks


In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.


### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.






### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?


### Result:
```python


#input
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


```




__________________________________________________________________________________




## Exercise 4: Primitive Quiz - 30 Marks


In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.


### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.


### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.


### Result:
```python
## Input


questions = [
    ("France", "Paris"),
    ("Germany", "Berlin"),
    ("Italy", "Rome"),
    ("Spain", "Madrid"),
    ("Portugal", "Lisbon"),
    ("Netherlands", "Amsterdam"),
    ("Belgium", "Brussels"),
    ("Austria", "Vienna"),
    ("Sweden", "Stockholm"),
    ("Denmark", "Copenhagen")
]


score = 0


for country, capital in questions:
    answer = input(f"What is the capital of {country}? ").strip()
    if answer.lower() == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {capital}.")
print(f"\nYour final score is {score} out of {len(questions)}.")


## Output


# What is the capital of France? PaRis
# Correct!
# What is the capital of Germany? bErLin
# Correct!
# What is the capital of Italy? rome
# Correct!
# What is the capital of Spain? MADRID
# Correct!
# What is the capital of Portugal? IDK
# Wrong! The correct answer is Lisbon.
# What is the capital of Netherlands? idk
# Wrong! The correct answer is Amsterdam.
# What is the capital of Belgium? Brussels
# Correct!
# What is the capital of Austria? Vienna
# Correct!
# What is the capital of Sweden? Stockholm
# Correct!
# What is the capital of Denmark? Copenhagen
# Correct!


# Your final score is 8 out of 10.


## Description
# 1. List of Questions: Each country and its capital are stored as pairs in a list.
# 2. Loop through Questions: For each question, the program asks the user for the capital of a country.
# 3. Check Answer: The program uses 'if' to check if the answer is correct, ignoring capitalization.
# 4. Provide Feedback: It gives feedback for each question (correct or wrong) and adds a score if correct.
# 5. Final Score: After the quiz, it prints the total score out of the number of questions.




print ("Welcome to Guess the Capital of Each City" )


for Quiz, correct_answer in Quiz: # The 'for' loop goes throught each question, asking and checking if the answer is correct
    answer = input(Quiz + " ")
    if answer.lower() == correct_answer.lower(): #This allows the user to input the word 'paris' in any form (eg: Paris, PaRis)


        print ("The answer you have given is correct. ")


    else: 
        print("The answer you have given is wrong. ")


print ("That is the end of the quiz, thank you. ")


```




___________________________________________________________________________________


## Exercise 5: Days of the Month - 30 Marks


Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.


### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.


### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.


### Result:
```python
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


```




____________________________________________________________________________________


## Exercise 6: Brute Force Attack - 30 Marks


Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.


### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.


### Optional Requirements:


Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.


### Result:
```python
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




```




_____________________________________________________________________________________


## Exercise 7: Some Counting - 20 Marks


Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case.
* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.
*You may include all loops in a single project*


### Result:
```python
## Input


# Loop 1:
print("Counting up from 0 to 50:")
for i in range(51):
    print(i)


# Loop 2:
print("\nCounting down from 50 to 0:")
for i in range(50, -1, -1):
    print(i)


# Loop 3:
print("\nCounting up from 30 to 50:")
for i in range(30, 51):
    print(i)


# Loop 4:
print("\nCounting down from 50 to 10 (steps of 2):")
for i in range(50, 9, -2):
    print(i)


# Loop 5:
print("\nCounting up from 100 to 200 (steps of 5):")
for i in range(100, 201, 5):
    print(i)


## Output
# Counting up from 0 to 50:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40
# 41
# 42
# 43
# 44
# 45
# 46
# 47
# 48
# 49
# 50


# Counting down from 50 to 0:
# 50
# 49
# 48
# 47
# 46
# 45
# 44
# 43
# 42
# 41
# 40
# 39
# 38
# 37
# 36
# 35
# 34
# 33
# 32
# 31
# 30
# 29
# 28
# 27
# 26
# 25
# 24
# 23
# 22
# 21
# 20
# 19
# 18
# 17
# 16
# 15
# 14
# 13
# 12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0


#Counting up from 30 to 50:
# 30
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40
# 41
# 42
# 43
# 44
# 45
# 46
# 47
# 48
# 49
# 50


# Counting down from 50 to 10 (steps of 2):
# 50
# 48
# 46
# 44
# 42
# 40
# 38
# 36
# 34
# 32
# 30
# 28
# 26
# 24
# 22
# 20
# 18
# 16
# 14
# 12
# 10


# Counting up from 100 to 200 (steps of 5):
# 100
# 105
# 110
# 115
# 120
# 125
# 130
# 135
# 140
# 145
# 150
# 155
# 160
# 165
# 170
# 175
# 180
# 185
# 190
# 195
# 200


## Description
# 1. 'range()':
# - Autimatically handles starting, stopping, and stepping.
# - For example, 'range(51)' counts from 0 to 50.
# 2. Step by step loops:
# - Loop 1: Counts up from 0 to 50.
# - Loop 2: Counts down from 50 to 0.
# - Loop 3: Counts up from 30 to 50.
# - Loop 4: Counts down from 50 to 10 in steps of 2.
# - Loop 5: Counts up from 100 to 200 in steps of 5.
# 3. 'print()' messages:
# - Each loop is preceded by a clear description of what it does.




```




___________________________
