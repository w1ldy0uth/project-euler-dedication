def even_fibonacci_sum(limit):
    a, b = 2, 8
    total = 0
    while a <= limit:
        total += a
        a, b = b, 4 * b + a
    return total

print(even_fibonacci_sum(4_000_000))

