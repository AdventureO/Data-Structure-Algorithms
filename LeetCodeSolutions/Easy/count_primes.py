import math


def count_primes(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return 0

    numbers = [i for i in range(n)]
    prime_count = sum([ 1 for number in numbers if is_prime(number)])
    return prime_count


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

print(count_primes(100))
