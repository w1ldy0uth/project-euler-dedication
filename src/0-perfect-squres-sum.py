def is_odd(n):
    return n % 2 == 1
  
def sum_perfect_squares(n):
  sum = 0
  for i in range(1, n + 1):
    square = i * i
    if is_odd(square):
      sum += square
  return sum

print(sum_perfect_squares(5)) # Output: 35 (1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35)
print(sum_perfect_squares(472000)) # Output: 17525674666588000