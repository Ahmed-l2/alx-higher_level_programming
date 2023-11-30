#!/usr/bin/python3.8.18
import hidden_4
for func in dir(hidden_4):
    if func[1] != "_":
        print(func)
