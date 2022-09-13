#!/usr/bin/python3

"""Export data in the JSON format"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    arg = int(argv[1])
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    parse_user = requests.get(users_url).json()

    for u in parse_user:
        if u.get("id") is arg:
            parse_todo = requests.get(todos_url).json()
            tasks = {u["id"]: []}

            for t in parse_todo:
                if t["userId"] is u["id"]:
                    tasks[u["id"]].append({"task": t["title"],
                                           "completed": t["completed"],
                                           "username": u["username"]})
            obj = json.dumps(tasks)
            with open("{}.json".format(arg), "w") as file:
                file.write(obj)
