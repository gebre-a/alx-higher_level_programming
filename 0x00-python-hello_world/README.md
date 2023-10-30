0x00. Python - Hello, World
Resource
The Python Tutorial (only the first three chapters below)
Whetting Your Appetite
Using the Python Interpreter
An Informal Introduction to Python (Read up until “3.1.2. Strings” included)
How to use string formatters in Python 3
Tasks
Run Python file : Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Holberton School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
Run inline : Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE
guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Holberton School: {}".format(88+10))'
Hello, print : Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print
Print integer : Complete the source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

You can find the source code here
The output of the script should be:
the number, followed by Battery street,
followed by a new line.
You are not allowed to cast the variable number into a string.
Your code must be 3 lines long
You have to use the new print numbers tips (with .format(...))
C is strongly typed… not in Python! The variable number can be assigned to a string, a float, a bool etc… Forcing the type during a string format ("...".format(...)) is a way to control the type of a variable

Print float : Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

You can find the source code here
The output of the program should be:
Float:, followed by the float with only two digits.
Followed by a new line.
You are not allowed to cast the variable number into a string.
You have to use the new print numbers tips (with .format(...))
Print string : Complete the source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

You can find the source code here
The output of the program should be:
3 times the value of str
followed by a new line
followed by the 9 first characters of str
followed by a new line
You are not allowed to use any loops or conditional statement
Your program should be maximum 5 lines long
Play with strings : Complete this source code to print Welcome to Holberton School!

You can find the source code here
You are not allowed to use any loops or conditional statements.
You have to use the variables str1 and str2 in your new line of code.
Your program should be exactly 5 lines long
Copy - Cut - Paste : Complete this source code.

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 8 lines long
word_first_3 should contain the first 3 letters of the variable word
word_last_2 should contain the last 2 letters of the variable word
middle_word should contain the value of the variable word without the first and last letters
Create a new sentence : Complete this source code to print object-oriented programming with Python, followed by a new line.

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 5 lines long
You are not allowed to create new variables
You are not allowed to use string literals
Easter Egg : Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py) 10 Linked list cycle Technical interview preparation:
You are not allowed to google anything
Whiteboard first
This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
Write a function in C that checks if a singly linked list has a cycle in it.
Prototype: int check_cycle(listint_t *list);
Return: 0 if there is no cycle, 1 if there is a cycle
Requirements:
Only these functions are allowed: write, printf, putchar, puts, malloc, free
Compile the code this way: gcc -Wall -Werror -Wextra -pedantic 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
Solving a problem is already a big win! but finding the best and optimal way to solve it, it’s way better! Think about the most optimal / fastest way to do it.
