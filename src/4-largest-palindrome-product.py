def is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]

def largest_palindrome_product() -> int:
    largest = 0

    for i in range(999, 99, -1):
        if i * 999 <= largest:
            break
        if i % 11 != 0:
            continue
        for j in range(999, i - 1, -1):
            product = i * j
            if product <= largest:
                break
            if is_palindrome(product):
                largest = product

    return largest

print(largest_palindrome_product())
