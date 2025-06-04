#!/usr/bin/python3
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing data if file exists; otherwise start with empty list
if os.path.exists(filename):
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []
else:
    items = []

# Add command-line arguments
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, filename)
