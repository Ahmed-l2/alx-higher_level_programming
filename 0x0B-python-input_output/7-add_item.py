#!/usr/bin/python3
"""Module for the 7th task"""

import sys
save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

arglist = list(sys.argv[1:])

try:
    jlist = load_json('add_item.json')
except Exception:
    jlist = []

jlist.extend(arglist)
save_json(jlist, 'add_item.json')
