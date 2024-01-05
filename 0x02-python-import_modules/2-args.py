#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    # Get the number of arguments
    num_arguments = len(argv) - 1  # Subtract 1 to exclude the script name

    # Print the number of arguments and the list of arguments

    print("Number of argument(s):", num_arguments, end=" ")
    if num_arguments == 0:
        print(".")
    else:
        print(":")

        # Print details for each argument
        for i in range(1, num_arguments + 1):
            print(f"{i}: {argv[i]}")
