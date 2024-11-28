"""
  Returns all divisors (factors) of a number.
"""

def get_factors(n):
  factors = set()
  for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
      factors.add(i)
      factors.add(n // i)
  return sorted(factors)

if __name__ == '__main__':
  print(get_factors(28))
