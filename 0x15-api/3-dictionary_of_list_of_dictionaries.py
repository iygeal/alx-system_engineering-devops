#!/usr/bin/python3
"""Python script that gathers data from an API and
    records all tasks from all employees to a JSON file
"""

import json
import requests

if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(user_url).json()

    output_dict = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        todo_url = f"{user_url}/{user_id}/todos"
        tasks = requests.get(todo_url).json()

        user_tasks = []
        for task in tasks:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            user_tasks.append(task_dict)

        output_dict[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(output_dict, json_file)
