import argparse


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


OPERATIONS = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
}


def main():
    parser = argparse.ArgumentParser(description='Simple calculator')
    parser.add_argument('operation', choices=OPERATIONS.keys(), help='Operation to perform')
    parser.add_argument('a', type=float, help='First number')
    parser.add_argument('b', type=float, help='Second number')
    args = parser.parse_args()

    result = OPERATIONS[args.operation](args.a, args.b)
    print(result)


if __name__ == '__main__':
    main()
