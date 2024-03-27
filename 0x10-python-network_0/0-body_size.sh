#!/bin/bash
# takes URL, sends request URL, displays size of the body of the response
curl -s -w "%{size_download}\n" -o /dev/null $1
