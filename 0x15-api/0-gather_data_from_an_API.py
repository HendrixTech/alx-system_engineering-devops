#!/usr/bin/python3
""" Accessing a REST API for todo lists of employees """

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employeeId = sys.argv[1]

    userResponse = requests.get(url + "users/{}".format(employeeId))
    employeeName = userResponse.json().get('name')
    
    todoUrl = url + "/users/{}/todos".format(employeeId)
    todoResponse = requests.get(todoUrl)

    tasks = todoResponse.json()
    done = 0
    completed = []

    for task in tasks:
        if task.get('completed'):
            completed.append(task)
            done += 1

    print("Eployee {} is done with tasks({}/{}):".format(employeeName,
        done, len(tasks)))

    for complete in completed:
        print("\t {}".format(complete.get('title')))
