#!/usr/bin/python3

"""Rest API of todo list"""

from sys import argv
import requests
import json

if __name__ == "__main__":
    """Print tasks done by employee id"""
    done = 0
    total = 0
    todo = []
    arg = int(argv[1])
    with requests.get('https://jsonplaceholder.typicode.com/users'
                      ) as response:
        data = response.text
        parse_json = json.loads(data)

    for u in parse_json:
        if u.get("id") is arg:
            with requests.get('https://jsonplaceholder.typicode.com/todos'
                              ) as res:
                d = res.text
                parse = json.loads(d)

                for task in parse:
                    if task.get("userId") is arg:
                        done += 1
                        if task.get("completed") is True:
                            todo.append(task.get("title"))
                            total += 1
            print("Employee {} is done with tasks({}/{}):"
                  .format(u.get("name"), total, done))
            for line in todo:
                print("\t{}".format(line))
