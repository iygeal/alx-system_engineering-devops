#!/usr/bin/python3
"""Python script that gathers data from an API and exports to json"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    base_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    res = requests.get(base_url).json()
    employee_name = res.get("name")

    todo_url = f"{base_url}/todos"
    tasks = requests.get(todo_url).json()

    username = res.get("username")

    with open(f"{user_id}.json", "w") as f:
        for task in tasks:
            task_list = [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username
                }
            ]
            data = {user_id: task_list}
            json.dump(data, f)
