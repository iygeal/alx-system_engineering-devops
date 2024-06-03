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
    username = res.get("username")

    todo_url = f"{base_url}/todos"
    tasks = requests.get(todo_url).json()

    output_dict = {user_id: []}

    for task in tasks:
        task_status = True if task.get("completed") else False
        task_title = task.get("title")
        task_dict = {
            "task": task_title,
            "completed": task_status,
            "username": username
        }
        output_dict[user_id].append(task_dict)

    with open(f"{user_id}.json", "w") as f:
        json.dump(output_dict, f)
