#!/usr/bin/python3
"""Module"""
from sys import requests
import requests
from requests.auth import HTTPBasicAuth


def gitHubCred():
    credauth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    d = r.json()
    print(d.get("id"))


if __name__ == "__main__":
    gitHubCred()
