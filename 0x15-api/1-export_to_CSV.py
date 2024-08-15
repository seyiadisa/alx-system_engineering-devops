#!/usr/bin/python3
"""Task 1"""
import csv
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
    filename = f"{employee_id}.csv"
    body, e_name = make_request(employee_id)

    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in body:
            row = [employee_id, e_name]
            row += [todo.get('completed'), todo.get('title')]
            writer.writerow(row)
