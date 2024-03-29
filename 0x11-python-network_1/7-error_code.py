#!/usr/bin/python3
"""Fetch"""
import requests
import sys


def fetch():
    """Fetches URL and display body or status code"""
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.HTTPError as err:
        if err.response.status_code >= 400:
            print("Error code: {}".format(err.response.status_code))


if __name__ == "__main__":
    fetch()