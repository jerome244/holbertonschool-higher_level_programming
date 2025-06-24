#!/usr/bin/python3
"""4-hidden_discovery.py: Prints names defined in the compiled hidden_4.pyc file."""

import marshal

if __name__ == '__main__':
    pyc_path = '/tmp/hidden_4.pyc'
    with open(pyc_path, 'rb') as f:
        # Skip the header (magic number, timestamp, etc.)
        f.read(16)
        code_obj = marshal.load(f)
    # Extract names from the code object
    names = [name for name in code_obj.co_names if not name.startswith('__')]
    for name in sorted(names):
        print(name)
