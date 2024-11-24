## Exercise 9: Hello - 10 Marks

# Fill in the blanks in the code below so that 
# the function hello() prints "Hello" to the console.

## Input 

def hello():
   print("Hello")

def main():
   hello()

if __name__ == "__main__":
    main()

## Output
# Hello

## Description
# 1. 'def hello()':
# - The 'print("Hello")' statement is used to print the word '"Hello"' 
# - to the console.
# 2. 'def main()':
# - 'hello()' is called, which executes the code inside the 'hello()' function.
# 3. 'if __name__ == "__main__"':
# - This line ensures that the 'main()' function is eecuted only when the script is 
# run directly (not when imported into another program).
# 4. Hot it works:
# - When you run the program, it executes 'main()'.
# - 'main()' calls 'hello()', and 'hello()' prints '"Hello"' to the console.