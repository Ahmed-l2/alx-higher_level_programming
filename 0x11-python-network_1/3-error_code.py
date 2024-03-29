#!/usr/bin/python3
"""fetches URL"""
import urllib.request
from sys import argv


def fetch():
    """Fetches body of reponse"""
    url = argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8')

        print(body)
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))


if __name__ == "__main__":
    fetch()
