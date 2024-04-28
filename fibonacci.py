def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)

    return fib_series
n = 10
result = fibonacci(n)
print(f"Fibonacci series of length {n}:")
print(result)
