#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io"""
import requests
from sys import argv


def fetch():
    """Fetches X-Request-Id variable"""
    url = argv[1]
    response = requests.get(url)

    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    fetch()
