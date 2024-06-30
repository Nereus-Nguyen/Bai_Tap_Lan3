from sympy import fibonacci

def get_fibonacci(n):
    return fibonacci(n)

# Tính số Fibonacci tại vị trí n
n = 10
fib_n = get_fibonacci(n)

print(f"Số Fibonacci thứ {n} là: {fib_n}")
