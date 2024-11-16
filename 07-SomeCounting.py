## Exercise 7: Some Counting - 20 Marks

# Use your newly acquired knowledge of the for loop to complete the following tasks.
# Print all values to the console in each case.
# Write a loop that counts up from 0 to 50 in increments of 1.
# Write a loop that counts down from 50 to 0 in decrements of 1.
# Write a loop that counts up from 30 to 50 in increments of 1.
# Write a loop that counts down from 50 to 10 in decrements of 2.
# Write a loop that counts up from 100 to 200 in increments of 5. 
# You may include all loops in a single project.

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