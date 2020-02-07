# from sympy import sieve
# primes = list(sieve.primerange(1, 10**6))

import math


def primerange(m, n):
    count = m

    while count < n:
        is_prime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                is_prime = False
                break
        if is_prime:
            print(count)

        count += 1

primerange(1000, 1000000)
