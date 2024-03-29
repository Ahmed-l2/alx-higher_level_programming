#!/usr/bin/python3
"""Fetch script"""
import requests
from sys import argv


def fetch():
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}

    response = requests.post(url, data=data)

    try:
        d = response.json()
        if not d:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except KeyError:
        print("Not a valid JSON")


if __name__ == "__main__":
    fetch()
