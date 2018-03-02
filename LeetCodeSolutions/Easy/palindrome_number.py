def is_palindrome_v1(x):
    """
    :type x: int
    :rtype: bool
    """
    str_x = str(x)
    len_x = len(str_x)
    if len_x % 2 == 0 and len_x >= 2:
        return str_x[:int(len(str_x)/2)] == str_x[int(len(str_x)/2):][::-1]
    elif len_x >= 3:
        return str_x[:int(len(str_x)/2)] == str_x[(int(len(str_x)/2) + 1):][::-1]
    else:
        return True


def is_palindrome_v2(x):
    """
    :type x: int
    :rtype: bool
    """
    return x == int(str(x)[::-1]) if x >= 0 else False


print(is_palindrome_v1(123321))
print(is_palindrome_v1(45654))
print(is_palindrome_v1(0))
print()
print(is_palindrome_v2(123321))
print(is_palindrome_v2(45654))
print(is_palindrome_v2(0))