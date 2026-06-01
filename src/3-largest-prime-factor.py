def get_largest_prime_factor(n):
  factors = []
  
  while n % 2 == 0:
    factors.append(2)
    n //= 2
  
  factor = 3
  while factor * factor <= n:
    while n % factor == 0:
      factors.append(factor)
      n //= factor
    factor += 2
  
  if n > 2:
    factors.append(n)
  
  return max(factors)

print(get_largest_prime_factor(13195)) # Output: 29
print(get_largest_prime_factor(600851475143)) # Output: 6857