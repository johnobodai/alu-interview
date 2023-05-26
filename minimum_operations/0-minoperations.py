#!/usr/bin/python3

def minOperations(n):
    """
    Calculates the minimum number of operations needed to obtain exactly 'n' occurrences of the character 'H' in a file.

    Args:
        n (int): The desired count of 'H' characters.

    Returns:
        int: The minimum number of operations required. Returns 0 if it is impossible to achieve 'n'.

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
