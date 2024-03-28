#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


def fetch():
    """Fetches given url"""
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        d = html.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(d)))
    print("\t- content: {}".format(html))


if __name__ == "__main__":
    fetch()
