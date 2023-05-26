#!/usr/bin/python3

def minOperations(n):
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
