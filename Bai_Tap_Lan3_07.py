# def prime_factors(number):
#     if number <= 1:
#         return False
#     if number <= 3:
#         return True
#     if number % 2 == 0 or number % 3 == 0:
#         return False
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number %(i + 2) == 0:
#             return False
#         i += 6
#     return True
# number = 21
# if prime_factors(number):
#     print(f"{number} là số nguyên tố.")
# else:
#     print(f"{number} không phải là số nguyên tố.")
def largest_prime_factor(n):
    # Bắt đầu với ước số nhỏ nhất là 2
    factor = 2
    largest_factor = 1

    while factor * factor <= n:
        if n % factor == 0:
            largest_factor = factor
            n //= factor
            # Chia hết cho đến khi không còn chia được nữa
            while n % factor == 0:
                n //= factor
        factor += 1

    # Nếu n còn lớn hơn 1 thì đó là ước số nguyên tố lớn nhất
    if n > 1:
        largest_factor = n

    return largest_factor

# Số cần tìm ước số nguyên tố lớn nhất
number = 600851475
print(f"Ước số nguyên tố lớn nhất của {number} là: {largest_prime_factor(number)}")
