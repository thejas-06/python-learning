def square(n):
    return n ** 2

def is_even(n):
    return n % 2 == 0

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result