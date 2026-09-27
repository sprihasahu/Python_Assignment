def check_prime(n):
    if n < 2:
        return False

    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1

    return True

if check_prime(17):
    print("Prime")
else:
    print("Not Prime")