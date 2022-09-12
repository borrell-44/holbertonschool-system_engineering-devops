#!/usr/bin/python3

"""Rest API of todo list"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    """Print tasks done by employee id"""
    done = 0
    total = 0
    todo = []
    arg = int(argv[1])
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    parse_json = requests.get(users_url).json()

    for u in parse_json:
        if u.get("id") is arg:
            parse = requests.get(todos_url).json()
            for task in parse:
                if task.get("userId") is arg:
                    done += 1
                    if task.get("completed") is True:
                        todo.append(task.get("title"))
                        total += 1
            print("Employee {} is done with tasks({}/{}):"
                  .format(u.get("name"), total, done))
            for line in todo:
                print("\t {}".format(line))
