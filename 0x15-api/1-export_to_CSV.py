#!/usr/bin/python3

"""Export data int the CSV format"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    data = []
    arg = int(argv[1])
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    parse_user = requests.get(users_url).json()

    for u in parse_user:
        if u.get("id") is arg:
            parse_todo = requests.get(todos_url).json()
            with open("{}.csv".format(arg), 'w') as csvfile:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                for t in parse_todo:
                    if t["userId"] is u["id"]:
                        writer.writerow([u["id"], u["username"],
                                         t["completed"], t["title"]])
