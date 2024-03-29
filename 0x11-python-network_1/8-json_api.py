#!/usr/bin/python3
"""Fetch script"""
import requests
from sys import argv


def fetch():
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 1:
        data = {'q': ""}
    else:
        data = {'q': argv[1]}

    response = requests.post(url, data=data)

    try:
        d = response.json()
        if not d:
            print("No result")
        else:
            print("[{}] {}".format(d.get("id"), d.get("name")))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    fetch()
