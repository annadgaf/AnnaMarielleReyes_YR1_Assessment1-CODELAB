## Exercise 4: Primitive Quiz - 30 Marks

# In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.
## Steps:
# 1. Write a program that asks the user "What is the capital of France?" and waits for their response.
# 2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
# 3. If the answer is incorrect, the program should print a message saying the answer is wrong.
## Advanced Requirements:
# Ignore Capitalization: Modify your program to accept answers regardless of the capitalization 
# (e.g., "paris", "Paris", and "PaRis" should all be considered correct). 
# Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries.
# Provide feedback for each question. 

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