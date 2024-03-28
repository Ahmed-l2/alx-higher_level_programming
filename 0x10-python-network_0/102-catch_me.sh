#!/bin/bash
#request to 0.0.0.0:5000/catch_me that cause server to respond with You got me!
curl -H "Origin: School" -sL -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
