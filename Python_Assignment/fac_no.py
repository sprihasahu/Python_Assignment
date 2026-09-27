def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"

    result = 1

    for number in range(1, n + 1):
        result *= number

    return result

print(factorial(5))  
print(factorial(0))  