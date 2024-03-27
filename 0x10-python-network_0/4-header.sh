#!/bin/bash
#takes URL as argument, sends GET request to URL, displays body of the response
curl -H "X-School-User-Id: 98" -sX GET "$1"
