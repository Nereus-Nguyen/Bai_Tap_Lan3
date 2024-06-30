def fibonacci (n):
    for i in range(n):
        if n < 0:
            return 0
        if n == 0 :
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            tong = fibonacci(n - 1) + fibonacci(n - 2)
        return tong
x = fibonacci(6)
print(x)



