"""
Factorial calculator for a positive integer.

Steps:
1) Define a function that computes factorial.
2) Pass a positive integer to the function.
3) Return the computed result and demonstrate usage.
"""

from typing import Final


def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a positive integer n (n >= 1).

    Args:
        n: A positive integer (e.g., 1, 2, 3, ...).

    Returns:
        The factorial of n as an integer.

    Raises:
        ValueError: If n is not a positive integer.
    """
    # ✅ Step 1: Validate the input is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer (n >= 1).")

    # ✅ Step 2: Initialize an accumulator for the product
    result: int = 1

    # ✅ Step 3: Multiply result by each integer from 2 up to n
    for i in range(2, n + 1):
        result *= i

    # ✅ Step 4: Return the computed factorial
    return result


def main() -> None:
    # ✅ Step 5: Provide an example input and call the function
    number_to_factor: Final[int] = 20 # You can change this value for testing
    factorial_value: int = calculate_factorial(number_to_factor)

    # ✅ Step 6: Present the result
    print(f"Factorial of {number_to_factor} is {factorial_value}")


if __name__ == "__main__":
    # ✅ Program entry point
    main()