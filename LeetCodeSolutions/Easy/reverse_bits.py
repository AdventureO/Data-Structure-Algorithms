def reverse_bits(n):
    origin = [2**i for i in range(32)]
    bit = []
    result = 0
    count = 31

    for i in reversed(origin):
        if n >= i:
            n -= i
            bit.append(1)
        else:
            bit.append(0)

    for i in reversed(bit):
        result += (i*(2**count))
        count -= 1

    return result


print(reverse_bits(43261596))