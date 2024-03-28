#!/bin/bash
#sends a JSON POST request to a URL and displays the body of the response.
curl -X POST -H "Content-Type: application/json" -d "@$2" "$1"
