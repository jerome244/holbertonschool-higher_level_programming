#!/usr/bin/python3
"""4-hidden_discovery.py: Prints names defined in the compiled module hidden_4.pyc located in /tmp."""

import marshal
import sys

if __name__ == "__main__":
    pyc_file = "/tmp/hidden_4.pyc"
    try:
        with open(pyc_file, "rb") as f:
            # Skip header: magic number (4 bytes), timestamp (4), size (4), flags (4)
            f.read(16)
            code_obj = marshal.load(f)
    except (FileNotFoundError, IOError):
        sys.exit(1)

    # Get all names from the code object excluding built-ins
    names = [name for name in code_obj.co_names if not name.startswith("__")]
    for name in sorted(names):
        print(name)
