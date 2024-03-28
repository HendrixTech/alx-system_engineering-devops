#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employeeId = sys.argv[1]

    userResponse = requests.get(url + "users/{}".format(employeeId))
    username = userResponse.json().get('username')

    todoUrl = url + "/users/{}/todos".format(employeeId)
    todoResponse = requests.get(todoUrl)

    tasks = todoResponse.json()

    dictionary = {employeeId: []}
    for task in tasks:
        dictionary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    with open('{}.json'.format(employeeId), 'w') as file:
        json.dump(dictionary, file)

