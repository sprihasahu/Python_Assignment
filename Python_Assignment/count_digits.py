def count_digits(n):
    n = abs(n)

    if n == 0:
        return 1

    digits = 0

    while n > 0:
        digits += 1
        n //= 10

    return digits

print(count_digits(12345))  
print(count_digits(-450))  