import dis
import sys


def main():
    # Load the compiled .pyc file into a code object
    with open(sys.argv[1], 'rb') as f:
        f.seek(16)  # Skip the .pyc header
        code = f.read()

    # Disassemble the code object
    names = set()
    for instruction in dis.get_instructions(code):
        if instruction.opname == 'LOAD_NAME':
            if not instruction.argval.startswith('__'):
                names.add(instruction.argval)
    
    # Sort the names alphabetically and print each on a new line
    for name in sorted(names):
        print(name)


if __name__ == "__main__":
    main()
