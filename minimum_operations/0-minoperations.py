#!/usr/bin/python3

"""
The min_operations module provides a function to calculate the minimum number of operations needed to obtain
a desired count of 'H' characters in a file.
"""

def minOperations(n):
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
    if n == 1:
        return 0

    num_operations = 0
    count = 1

    while count < n:
        if n % count == 0:
            num_operations += n // count
            count *n // count
        else:
            num_operations += count
            count += count

    if count == n:
        return num_operations
    else:
        return 0
