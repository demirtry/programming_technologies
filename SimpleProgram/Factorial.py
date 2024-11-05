def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of a number using recursion.
    Arg: n (int): The number for which to calculate the factorial.
    Returns: (int) The factorial of the given number.
    """
    try:
        if n < 0:
            return -1
        elif n == 0:
            return 1
        else:
            return n * factorial_recursive(n - 1)
    except ValueError:
        raise ValueError("Input must be >= 0.")
