def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers
    return average

grades = [90, 85, 92, 78, 80]
average_grade = calculate_average(grades)
print("Average Grade:", average_grade)

# (I encountered an issue where the debugger failed even after fixing the syntax error. This happened because my project contained a file named code.py, which conflicted with Python’s built-in code module that pdb imports internally. Python loaded my local file instead of the standard library module, causing the syntax error to persist. Renaming the file resolved the issue. This taught me the importance of avoiding filenames that shadow standard Python modules.)