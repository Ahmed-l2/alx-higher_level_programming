#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io"""
import urllib.request
from sys import argv


def fetch():
    """Fetches X-Request-Id variable"""
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        content = response.getheader("X-Request-Id")

    print(content)


if __name__ == "__main__":
    fetch()
