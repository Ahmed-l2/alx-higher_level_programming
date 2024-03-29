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

    d = response.json()
    if not d:
        print("No result")
    else:
        try:
            print("[{}] {}".format(d['id'], d['name']))
        except KeyError:
            print("Not a valid JSON")


if __name__ == "__main__":
    fetch()
