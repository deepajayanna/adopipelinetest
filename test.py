# This is the script to add two numbers 
# add_numbers.py

import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python add_numbers.py <num1> <num2>")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        total = a + b
        print(f"The sum of {a} and {b} is: {total}")
    except ValueError:
        print("Error: both inputs must be numbers")
        sys.exit(1)

if __name__ == "__main__":
    main()
