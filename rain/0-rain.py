#!/usr/bin/python3
"""
rainwater.py
This module provides a function for calculating the amount of rainwater
retained between walls represented as a relief map.
"""


def rain(walls):
    """
    Calculate the amount of rainwater retained between walls represented as
    a relief map.

    Parameters:
    - walls (list): A list of non-negative integers representing the heights
      of walls with unit width 1.

    Returns:
    - Integer: The total amount of rainwater retained.

    Functionality:
    - The walls list represents the cross-section of a relief map, where each
      integer represents the height of a wall with unit width 1.
    - The ends of the list (before index 0 and after index walls[-1]) are not
      considered as walls and will not retain water.
    - If the list is empty, the function returns 0.
    """
    if not walls:
        return 0

    total_water = 0
    left_max = [0] * len(walls)
    right_max = [0] * len(walls)

    left_max[0] = walls[0]
    for i in range(1, len(walls)):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[-1] = walls[-1]
    for i in range(len(walls) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    for i in range(1, len(walls) - 1):
        height = min(left_max[i], right_max[i])
        water = height - walls[i]
        total_water += water

    return total_water
