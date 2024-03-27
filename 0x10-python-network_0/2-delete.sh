#!/bin/bash
#sends DELETE request to URL passed as first argument and displays body of response
curl -s -X DELETE "$1"
