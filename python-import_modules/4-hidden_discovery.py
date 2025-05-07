#!/usr/bin/python3
import marshal
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    with open(sys.argv[1], 'rb') as f:
        f.seek(16)
        code = marshal.load(f)

    names = [name for name in code.co_names if not name.startswith('__')]
    for name in sorted(names):
        print(code.co_names)
