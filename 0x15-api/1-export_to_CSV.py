#!/usr/bin/python3
"""Python script that gets from an API and exports to CSV"""

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

    with open(f"{user_id}.csv", "w") as f:
        for task in tasks:
            task_status = "True" if task.get("completed") else "False"
            task_title = task.get("title")
            f.write(
                '"{}","{}","{}","{}"\n'.format(
                    user_id, username, task_status, task_title))
