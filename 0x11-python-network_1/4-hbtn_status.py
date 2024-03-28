#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests


def fetch():
    """Fetches given url"""
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    fetch()
