#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

def fetch():
    """Fetches given url"""
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        d = html.decode('utf-8')

    print("Body response:$")
    print("    - type: {}$".format(type(html)))
    print("    - content: {}$".format(html))
    print("    - utf8 content: {}$".format(d))

if __name__ == "__main__":
    fetch()
