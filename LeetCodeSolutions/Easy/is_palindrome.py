import re


def is_palindrome(s):
    reversed_string = re.sub(r'[^a-zA-Z0-9\s]', '', s.lower().replace(" ", ""))
    return reversed_string[::-1] == reversed_string


print(is_palindrome("man, a plan, a canal: Panama"))
