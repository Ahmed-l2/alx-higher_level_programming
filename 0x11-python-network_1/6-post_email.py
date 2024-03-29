#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io"""
import requests
from sys import argv


def fetch():
    """Fetches X-Request-Id variable"""
    url = argv[1]

    data = {'email': argv[2]}
    response = requests.post(url, data=data)

    print(response.text)


if __name__ == "__main__":
    fetch()
