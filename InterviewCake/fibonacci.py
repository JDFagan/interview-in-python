# Not great recursive solution: O(2^n) time and O(2^n) space
def fib_recursive(n):
    if n < 0:
        raise IndexError("No such valid Fibonacci value for negative number")
    if n in [0, 1]:
        return n

    print("computing fib_recursive({})".format(n))
    return fib_recursive(n - 2) + fib_recursive(n - 1)
