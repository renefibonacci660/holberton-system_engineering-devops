#!/usr/bin/python3
""" Uses provided RESTful API to return employee todo progress info """
import requests
import sys


def complete_req():
    """ Completes request with provided info """
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user_info = requests.get("{}/users/{}".format(url, user_id)).json()
    todo_dict = requests.get("{}/todos?userId={}".format(url, user_id)).json()
    username = user_info.get("name")
    completed = []
    for task in todo_dict:
        if task["completed"]:
            completed.append(task["title"])
    print("Employee {} is done with tasks({}/{}):".format(username, len(
        completed), len(todo_dict)))
    for task in completed:
        print("\t {}".format(task))

if __name__ == "__main__":
    complete_req()
