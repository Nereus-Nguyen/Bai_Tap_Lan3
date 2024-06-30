def UCLN (x,y):
    while y != 0:
        x,y = y, x%y
    return x
a = 0
b = 3

print(f"uoc chung lon nhat cua {a} va {b} la {UCLN(a, b)}")
