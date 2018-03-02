def is_power_of_three(n):
    """
    :type n: int
    :rtype: bool
    """
    while n > 1:
        if n % 3 == 0:
            n /= 3
        else:
            return False

    return n == 1

print(is_power_of_three(9))
print(is_power_of_three(81))
print(is_power_of_three(21))