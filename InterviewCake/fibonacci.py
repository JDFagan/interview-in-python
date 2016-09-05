# Not great recursive solution: O(2^n) time and O(2^n) space
def fib(n):
    if n < 0:
        raise IndexError("No such valid Fibonacci value for negative number")
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-2) + fib(n-1)
