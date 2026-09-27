def sum_natural(n):
    total = 0

    for number in range(1, n + 1):
        total += number

    return total

print(sum_natural(10))  