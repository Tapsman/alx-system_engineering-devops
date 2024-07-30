#!/usr/bin/python3
"""This is a function that returns an ID information for given emplyee"""
import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userID": sys.argv[1]}).json()

    """The complete"""
    complete = [t.get("title") for t in todos if t.get("complete") is True]
    print("The Employee {} is done with the tasks({}/{}):".format(
        user.get("name"), len(complete), len(todos)))
    [print("\t {}".format(c)) for c in complete]