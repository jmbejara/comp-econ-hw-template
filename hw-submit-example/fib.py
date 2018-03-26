def fib(n):
    """Compute the `n`-th number in the sequence of Fibonnaci numbers.
    """
    assert n >= 0
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fib(n-1)+fib(n-2)