#!/usr/bin/python3
import sys
import marshal
import os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    pyc_path = sys.argv[1]
    if not os.path.isabs(pyc_path):
        pyc_path = os.path.join(os.getcwd(), pyc_path)

    with open(pyc_path, 'rb') as f:
        f.seek(16)
        code = marshal.load(f)

    names = [name for name in code.co_names if not name.startswith('__')]
    for name in sorted(names):
        print(name)
