def fibonacci(n):
    y = (1 + 5 ** (1 / 2)) / 2
    x = (1 - 5 ** (1 / 2)) / 2
    return (y**n - x**n) / (5**(1/2))
