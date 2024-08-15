#!/usr/bin/python3
"""Task 0"""
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
    body, e_name = make_request(employee_id)
    todo_str = ""
    complete_count = 0

    for todo in body:
        if todo.get('completed'):
            todo_str += f"\t {todo.get('title')}\n"
            complete_count += 1

    task_ratio = complete_count / len(body)
    sys.stdout.write(f"Employee {e_name} is done with tasks({task_ratio}):\n")
    sys.stdout.write(todo_str)
