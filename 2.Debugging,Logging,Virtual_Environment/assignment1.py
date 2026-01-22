# Debugging Techniques and Tools
# Proble Statement:

# code.py file contains a Python program that contains deliberate bugs or errors. These bugs could include syntax errors, logical errors, or runtime errors.
# Use the Python debugger (pdb) to step through the program, identify the bugs, and fix them. Document the bugs you encountered and the steps you took to resolve them.
# Implement at least three different debugging techniques, such as adding print statements, using breakpoints, or using a visual debugger like PyCharm or VS Code. Compare their effectiveness and document your findings.
# Write a short reflection on your experience with debugging. Discuss the challenges you faced, the strategies that worked well for you, and any insights you gained from this assignment.

# First bug: Syntax error in the calculate_average function
# average = total / len(numbers
#                          ^
# SyntaxError: '(' was never closed

# bug/error fix :

# def calculate_average(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     average = total / len(numbers)  # Fixed the syntax error by closing the parenthesis
#     return average
# grades = [90, 85, 92, 78, 80]
# average_grade = calculate_average(grades)   
# print("Average Grade:", average_grade)

# Debugging Technique 1 → Print Statements

# Add prints to track values:

def calculate_average(numbers):
    total = 0
    print("Numbers:", numbers)
    for number in numbers:
        print("Adding:", number)
        total += number
        print("Total so far:", total)
    average = total / len(numbers)
    print("Final Average:", average)
    return average
grades = [90, 85, 92, 78, 80]
average_grade = calculate_average(grades)


# Debugging Technique 2 → Using pdb
# To use pdb, run the script from the command line with:
# python -m pdb code_debug.py

# Second Bug Found (pdb Not Starting)

# Even after fixing the syntax error, pdb was still showing the same error.
# The traceback showed:

# File "... \code.py", line 5


# Cause:
# I had a file named code.py in my project directory.
# The pdb module internally imports Python’s built-in code module, but Python was importing my local code.py instead. This caused a conflict (module shadowing).

# Fix:
# Renamed:

# code.py → code_debug.py


# Restarted the terminal and ran again:

# python -m pdb assignment1.py

# Now the debugger started successfully.

# Debugging Technique 3 → Visual Debugger (VS Code)
# Open the code_debug.py file in VS Code.   
# Set breakpoints by clicking in the gutter next to the line numbers.
# Start debugging by pressing F5 or selecting "Run and Debug" from the Run menu.


#########################################################################################################

# Debugging Techniques Used

# Print Statements (Manual Debugging)
# I added print statements inside the function to observe how values changed during execution.

# def calculate_average(numbers):
#     total = 0
#     print("Numbers:", numbers)
#     for number in numbers:
#         print("Current number:", number)
#         total += number
#         print("Total so far:", total)
#     average = total / len(numbers)
#     print("Calculated average:", average)
#     return average
# grades = [90, 85, 92, 78, 80]
# average_grade = calculate_average(grades)
# print("Average Grade:", average_grade)]


# This helped me understand:

# Whether the loop was running correctly

# How total was changing after each iteration

# If the final average was computed properly


# Python Debugger (pdb)

# I ran the program using:

# python -m pdb assignment1.py


# Commands used:

# l → show code

# n → next line

# s → step into function

# p variable → print variable

# c → continue

# Example:

# (Pdb) s
# (Pdb) p total
# (Pdb) n
# (Pdb) p number


# This allowed me to:

# Execute code line by line

# Inspect variables at precise moments

# Understand scope and execution flow


# VS Code Debugger (Visual Debugging)

# Steps:

# Open assignment1.py in VS Code

# Click next to a line number to add a breakpoint

# Press F5 → Start Debugging

# Observe:

# Variables panel

# Call Stack

# Step Over / Step Into

# This made debugging:

# Very visual

# Easier to understand

# Faster to find mistakes

# Reflection on Debugging Experience :

# This debugging assignment helped me realize that errors are not always only in code but can also come from environment issues such as file naming conflicts. Initially, syntax errors and NameError messages were confusing, but stepping through the program using pdb made execution flow much clearer. Print statements were useful for quickly checking variable values, while the VS Code debugger was the most effective because of its visual interface. I learned that understanding variable scope and execution order is critical in debugging. Combining multiple debugging techniques made problem-solving faster and more systematic. Debugging is not just about fixing bugs but about deeply understanding how a program works.
