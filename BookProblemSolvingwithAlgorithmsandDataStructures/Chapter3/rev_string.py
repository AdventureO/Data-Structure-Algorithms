from stack_v1 import Stack


def rev_string(my_str):

    s = Stack()
    for i in my_str:
        s.push(i)

    reverse_str = ''
    for i in range(s.size()):
        reverse_str += s.pop()

    return reverse_str

print(rev_string("adventure"))