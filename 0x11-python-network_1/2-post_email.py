#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io"""
import urllib.request
import urllib.parse
from sys import argv


def fetch():
    """Fetches X-Request-Id variable"""
    url = argv[1]

    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email).encode()

    request = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(request)

    print(response.read().decode())


if __name__ == "__main__":
    fetch()
