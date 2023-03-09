#!/usr/bin/python3
if __name__ == "__main__":
    """print the addition of all arguments."""
    import sys

    n = len(sys,argv)

    total = 0

    for i in range(1, n):
        total += int(sys.argv[i])
        print(f"{total}")
