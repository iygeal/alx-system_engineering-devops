#!/usr/bin/python3
"""Python script that gathers data from an API"""

import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    base_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    res = requests.get(base_url).json()
    employee_name = res.get("name")

    todo_url = f"{base_url}/todos"
    tasks = requests.get(todo_url).json()

    done = 0

    for task in tasks:
        if task.get("completed"):  # if task is completed
            done += 1  # add 1 to done

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done, len(tasks)))
    for task in tasks:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
