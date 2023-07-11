#!/usr/bin/python3
"""
Module containing add_attribute function
"""


json = __import__("json")
sys = __import__("sys")
save_to_json_file = __import__('5-save_to_json_file.py').\
    save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py')\
    .load_from_json_file


"""
Something
Something
"""
try:
    existing_items = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_items = []

"""
Other
"""
new_items = sys.argv[1:]
updated_items = existing_items + new_items

save_to_json_file(updated_items, "add_item.json")
