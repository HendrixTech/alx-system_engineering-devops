#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
"""

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

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                    .format(employeeId, username, task.get('completed'),
                        task.get('title')))
