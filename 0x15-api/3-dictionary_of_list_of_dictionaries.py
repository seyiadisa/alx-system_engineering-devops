#!/usr/bin/python3
"""Task 3"""
import json
import requests
import sys


def make_request(e_id):
    """
    Helper function to make HTTP requests to the API

    Args:
        enpoint: API endpoint
        e_id: employee id
    """
    url = "https://jsonplaceholder.typicode.com"
    res = requests.get(f"{url}/todos")
    name = requests.get(f"{url}/users/{e_id}").json().get('name')
    return res.json(), name


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Enter a command line argument")

    employee_id = sys.argv[1]
    filename = "todo_all_employees.json"
    body, e_name = make_request(employee_id)
    users = {}
    todos = []

    for todo in body:
        if users.get(todo.get("userId")) is None:
            users[todo.get("userId")] = []
        else:
            new_dict = dict()
            new_dict["username"] = e_name
            new_dict["task"] = todo.get('title')
            new_dict["completed"] = todo.get('completed')
            users[todo.get("userId")].append(new_dict)

    with open(filename, "w") as file:
        json.dump(users, file)
