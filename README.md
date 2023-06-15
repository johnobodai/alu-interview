# Rainwater Retention

This repository contains a Python function for calculating the amount of rainwater retained between walls represented as a relief map.

## Function

The function `rain(walls)` takes a list of non-negative integers representing the heights of walls and returns the total amount of rainwater retained. The function follows the following rules:

- The walls list should represent the cross-section of a relief map, where each integer represents the height of a wall with unit width 1.
- The ends of the list (before index 0 and after index `walls[-1]`) are not considered as walls and will not retain water.
- If the list is empty, the function returns 0.

## Usage

1. Clone the repository to your local machine:

git clone <repository-url>

2. Import the `rain` function into your Python project:
```python
from rainwater import rain

    Call the rain function with a list of non-negative integers representing the heights of walls:

    python

    walls = [3, 0, 2, 1, 4]
    total_water = rain(walls)
    print("Total water retained:", total_water)
```

    This will calculate the total amount of water retained between the walls and print the result.

## Contributing

Contributions are welcome! If you find any issues with the function or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
