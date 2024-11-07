def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of a number using recursion.
    Arg: n (int): The number for which to calculate the factorial.
    Returns: (int) The factorial of the given number.
    >>> factorial_recursive(-1)
    -1
    >>> factorial_recursive(0)
    1
    >>> factorial_recursive(1)
    1
    >>> factorial_recursive(5)
    120
    >>> factorial_recursive(10)
    3628800
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
