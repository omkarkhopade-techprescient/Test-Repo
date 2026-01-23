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