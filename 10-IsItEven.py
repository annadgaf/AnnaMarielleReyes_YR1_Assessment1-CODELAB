## Exercise 10: Is it even? - 35 Marks

# Write a program that tests if a value is even or odd. 
# Follow the instructions outlined below:
## Instructions:
# - The program should ask the user for a number from within the main function.
# - The entered number should be passed to a function that determines if the value is even or odd.
# - The function should return a message indicating whether the number is even or odd.
# - The message returned by the function should be printed from within the main function.

## Input

def check_even_or_odd(number):
    if number % 2 == 0: 
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    num = int(input("Enter a number: "))
    result = check_even_or_odd(num)
    print(result)

if __name__ == "__main__":
    main()

## Output
# Enter a number: 5
# 5 is odd.
# Enter a number: 4
# 4 is even.
# Enter a number: 3
# 3 is odd.
# Enter a number: 2
# 2 is even.
# Enter a number: 1
# 1 is odd.

## Description
# 1. 'check_even_or_odd(number)' Function:
# - This function takes a number as input.
# - It checks if the number is even using the '%'.
# - If 'number % 2 == 0', the number is even.
# - Otherwise, it's odd.
# - It then returns a message, like '"4 in even."' or '"7 is odd."'.
# 2. 'main()' Function:
# - The program asks the user to enter a number using 'input()'.
# - It converts the input to an integer using 'int()'.
# - The number is passed to the 'check_even_or_odd()' function to determine if it's even or odd.
# - The result is printed to the console.
# 3. 'if __name__ == "__main__"':
# - This ensures that the 'main()' function runs only if the file is eecuted directly.x