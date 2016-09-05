# Naive recursive solution: O(2^n) time and O(2^n) space
def fib_recursive(n):
    if n < 0:
        raise IndexError("No such valid Fibonacci value for negative number")
    if n in [0, 1]:
        return n

    print("computing fib_recursive({})".format(n))
    return fib_recursive(n - 2) + fib_recursive(n - 1)


# Smart recursive solution that uses memoization to cache expensive calculations bottom up
# O(n) time and O(1) space
class Fibonacci:
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        # Edge case
        if n < 0:
            raise IndexError("No such valid Fibonacci value for negative number")

        # Base cases
        if n in [0, 1]:
            return n

        # See if we've already calculated this before
        if n in self.memo:
            print("Grabbing memo[{}]".format(n))
            return self.memo[n]

        # Compute it
        print("Computing fib({})".format(n))
        result = self.fib(n - 1) + self.fib(n - 2)

        # Memoize
        self.memo[n] = result

        return result
