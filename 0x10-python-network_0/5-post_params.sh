#!/bin/bash
#takes URL as argument, sends POST request to URL, display body of the response
curl -d "email=test@gmail.com" -d "subject=I will always be here for PLD" -X POST "$1"
