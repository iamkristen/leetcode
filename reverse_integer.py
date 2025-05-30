def reverse_integer(num):
    sign = -1 if num < 0 else 1
    reverse_num = 0
    num = abs(num)

    while num > 0:
        current = num%10
        num //=10
        reverse_num = reverse_num*10+current
    reverse_num *= sign
    if reverse_num > (2 ** 31) - 1 or reverse_num < -2 ** 31:
        reverse_num = 0
    return reverse_num


num = 12345534
print(reverse_integer(num))