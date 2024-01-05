#!/usr/bin/python3

# filename: add_arguments.py
if __name__ == "__main__":
    from sys import argv

    # Get the command-line arguments (excluding the script name)
    arguments = argv[1:]

    # Convert arguments to integers and calculate the sum
    total = sum(int(arg) for arg in arguments)

    # Print the result
    print(total)
