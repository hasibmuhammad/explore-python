# Factorial = 5
#     5 * 4 * 3 * 2 * 1
# Factorial = 6
#     6 * 5 * 4 * 3 * 2 * 1
# Factorial = 7
#     7 * 6 * 5 * 4 * 3 * 2 * 1

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact

print(factorial(5))