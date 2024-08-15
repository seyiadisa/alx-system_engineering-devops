#!/usr/bin/python3
"""Task 2"""
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
    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(f"{url}/{e_id}/todos")
    name = requests.get(f"{url}/{e_id}").json().get('name')
    return res.json(), name


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Enter a command line argument")

    employee_id = sys.argv[1]
    filename = f"{employee_id}.json"
    body, e_name = make_request(employee_id)
    todos = []

    for todo in body:
        new_dict = dict()
        new_dict["task"] = todo.get('title')
        new_dict["completed"] = todo.get('completed')
        new_dict["username"] = e_name
        todos.append(new_dict)

    with open(filename, "w") as file:
        json.dump({str(employee_id): todos}, file)
