#!/bin/bash
#takes URL as argument, sends POST request to URL, display body of the response
curl -d "email=test@gmail.com
        subject=I will always be here for PLD" -sX POST "$1"
