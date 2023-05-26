#!/usr/bin/python3

"""
Module: min_operations

The min_operations module provides a function to calculate the minimum number of operations needed to obtain
a desired count of 'H' characters in a file.

"""


def min_operations(n):
    """
    Calculates the minimum number of operations needed to obtain exactly 'n' occurrences of the character 'H' in a file.

    Args:
        n (int): The desired count of 'H' characters.

    Returns:
        int: The minimum number of operations required. Returns 0 if it is impossible to achieve 'n'.

    Examples:
        >>> min_operations(1)
        0
        >>> min_operations(3)
        3
        >>> min_operations(6)
        5
        >>> min_operations(9)
        6
    """

    if n <= 1:
        return 0

    operations = float('inf')
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            operations = min(operations, i + min_operations(n // i))

    if operations == float('inf'):
        return n

    return operations


if __name__ == '__main__':
    # Example usage
    n = 9
    result = min_operations(n)
    print(f"Number of operations to obtain {n} 'H' characters: {result}")

