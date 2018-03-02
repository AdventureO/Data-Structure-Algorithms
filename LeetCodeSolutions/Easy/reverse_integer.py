def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    neg_limit = -0x80000000
    pos_limit = 0x7fffffff

    str_x = str(x)
    if x < 0:
        x = -int(str_x[1:][::-1])
        return x if x & neg_limit == neg_limit else 0

    else:
        x = int(str_x[::-1])
        return x if x & pos_limit == x else 0


print(reverse(-210))
print(reverse(1534236469))
print(reverse(0))
