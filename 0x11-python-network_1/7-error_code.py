#!/usr/bin/python3
"""Fetch"""
import requests
import sys


def fetch():
    """Fetches URL and display body or status code"""
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print('Error code:', response.status_code)
    else:
        print(response.text)


if __name__ == "__main__":
    fetch()
