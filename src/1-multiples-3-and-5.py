def is_multiple_of_3_or_5(n):
    return n % 3 == 0 or n % 5 == 0

def sum_of_multiples(n):
  sum = 0
  for i in range(1, n):
    if is_multiple_of_3_or_5(i):
      sum += i
  return sum

print(sum_of_multiples(10)) # Output: 23 (3 + 5 + 6 + 9 = 23)
print(sum_of_multiples(1000)) # Output: 233168