"""
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


print(fatorial(5))
"""


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = 40
print(f"Fibonacci de {num} = {fibonacci(num)}")
