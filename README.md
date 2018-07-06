# Python Tutorial
This tutorial is aimed to practice core functions of Python. The project is created using PyCharm and organising the packages in the easy to follow steps.

# Fundamental

## Get Started - package 01_get_started
### hello_world.py
Starts off with classic hello world application, using print function.

### hello_function.py
Python runs on an interpreter system, however it can be treated in a procedural way, an object-orientated way or a functional way.
In Python a function is defined using the def keyword with parenthesis and optional parameters terminated with : at the end. 

Python interpreter relies heavily on indentations to indicate a block of code as we can see from the implementation of my_function.
This rule is also applied to conditional statements and loops which is very important as you may find yourself in trouble trying to fix bug or error caused by incorrect indentations.

### Comments - comments.py
Python uses hash sign (#) to begin a comment. All characters after the # and up to the end of the physical line are part of the comment

### Quotation - quotation.py
Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.

### User Input - user_input.py
Some basic built-in function provided in order to interact with user.

### Multi-Line Statement - multiline_statement.py
It uses backslash (\) to denote that the line should continue

### Multiple Statement Single Line - multiple_statement_singleline.py
The semicolon ( ; ) allows multiple statements on the single line given that neither statement starts a new code block.

## Variables - package 02_variables
### Variable Declaration - variable_declaration.py
Python does not require you to declare variable explicitly. It happens automatically when assigning value to variable using = operator with the value on the right hand.

### Multiple Assignment - multiple_assignment.py
Python allows you to assign a single value to several variables simultaneously. The sample demonstrates that all three variables are assigned to the same memory location (pointer).
The del function is used to delete the reference pointer.

### Numeric - numerical_types.py
Python supports four numerical data type below. The type can be defined explicitly for Long and Complex.  
- int (signed integers)
- long (long integers, they can also be represented in octal and hexadecimal)
- float (floating point real values)
- complex (complex numbers)

### List - list_type.py
A list contains items separated by commas and enclosed within square brackets ([]) similar to arrays in other languages. However, all the items belonging to a list can be of different data type.
The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator.

### String - string_type.py
Strings in Python are identified as a contiguous set of characters represented in the quotation marks. Technically, a String can be considered as a list of characters.
Python allows us to use the same operators as list, such as [], [:], +, *  

### Tuple - tuple_type.py
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

### Dictionary - dict_type.py
Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.

## Operators - package 03_operators
### arithmetic_operators.py
Python supports these arithmetic operators, addition, subtraction, multiplication, division, modulus, exponent, floor division

### Comparison Operators - comparison_operators.py
Python supports these comparison operators, ==, !=, <>, >, <, >=, <=

### Assignment Operators - assignment_operators.py
Python supports these assignment operators, =, +=, -=, *=, /=, %=, **=, //=

### Membership Operators - membership_operators.py
Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples.

### Identity Operators - identity_operator.py
Identity operators compare the memory locations of two objects.

## Decision Making and Loop - package 04_decision_making_and_loop
### If/Else - if_else.py
Python programming language assumes any non-zero and non-null values as TRUE, and if it is either zero or null, then it is assumed as FALSE value.

### While and For Loop - while_loop.py, for_loop.py
Iterating by Sequence Index
With for-loop, an alternative way of iterating through each item is by index offset into the sequence itself

Python supports to have an else statement associated with a loop statement

- If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list.

- If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

## Numbers - package 05_numbers

### Number Type Conversion - type_conversion.py
Python converts numbers internally in an expression containing mixed types to a common type for evaluation. But sometimes, you need to coerce a number explicitly from one type to another to satisfy the requirements of an operator or function parameter.

### Mathematical Functions - mathematic_functions.py
Python includes a number of functions that perform mathematical calculations.

### Random Number Functions - random_functions.py
Random numbers are used for games, simulations, testing, security, and privacy applications. 