# Working with Virtual Environments, Pip, and PyPI
# Problem Statements:

# Research and understand the concept of virtual environments in Python. Learn how to create and activate a virtual environment using tools like venv or conda.
# Create a new virtual environment for this assignment and activate it.
# Identify a Python library or module from PyPI that you would like to use in your project. For this assignment, let's choose the "requests" library, which is commonly used for making HTTP requests
# Use pip to install the “requests” library into your virtual environment.
# Write a Python program that leverages the installed library to make an API call to a free API available on the internet. You can choose any API that suits your interests or requirements. Here's an example API that gives random todo tasks: https://jsonplaceholder.typicode.com/todos/1
# Document the steps you took to install the library, any issues encountered, and how you resolved them.
# Reflect on the benefits of using virtual environments and package management tools like pip. Discuss how they contribute to better code organization, maintainability, and collaboration.
# Share your program and virtual environment configuration files (e.g., requirements.txt) to demonstrate the successful installation and usage of the library. This ensures that others can recreate your environment and run your program without issues.

################################################################################################################################################################################

# Program to make an API call using the requests library

import requests

def fetch_todo():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    
    if response.status_code == 200:
            todo = response.json()
            print("Todo Task:")
            print(f"ID: {todo['id']}")
            print(f"Title: {todo['title']}")
            print(f"Completed: {todo['completed']}")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

if __name__ == "__main__":
    fetch_todo()

# Steps Taken to Install the Library:
# 1. Created a virtual environment using the command:   python -m venv myenv
# 2. Activated the virtual environment: 
#    - On Windows: myenv\Scripts\activate
#    - On macOS/Linux: source myenv/bin/activate
# 3. Installed the requests library using pip: pip install requests
# 4. Verified the installation by running the program above.
# Issues Encountered:
# - No major issues were encountered during the installation process. If any issues arise, they can often be resolved by ensuring that pip is up to date using: pip install --upgrade pip
# Benefits of Using Virtual Environments and Package Management Tools:
# - Virtual environments allow for isolated project dependencies, preventing conflicts between different projects.

# - They enhance code organization by keeping project-specific packages contained.
# - Package management tools like pip simplify the installation and management of libraries, making it easier to share and collaborate on projects.
# - Using a requirements.txt file allows others to recreate the same environment easily by running: pip install -r requirements.txt
# Virtual Environment Configuration File (requirements.txt):
# requests==2.31.0  # (The version may vary based on the latest available version at the time of installation)  

# To create the requirements.txt file, run the command: pip freeze > requirements.txt
# This file can be shared along with the project to ensure others can install the same dependencies.    
