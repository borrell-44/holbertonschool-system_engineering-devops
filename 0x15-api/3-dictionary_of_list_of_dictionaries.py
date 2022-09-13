#!/usr/bin/python3

"""Export all data in the JSON format"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    data = {}
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    parse_user = requests.get(users_url).json()
    parse_todo = requests.get(todos_url).json()

    for u in parse_user:
        data[u["id"]] = []

        for t in parse_todo:
            if t["userId"] is u["id"]:
                data[u["id"]].append({"username": u["username"],
                                      "task": t["title"],
                                      "completed": t["completed"]})
    obj = json.dumps(data)
    with open("todo_all_employees.json", "w") as file:
        file.write(obj)
