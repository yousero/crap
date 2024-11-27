
"""
  Limit array elements by number of occurrences.
"""

def limit(arr, n):
  counts = {}
  result = []
  for value in arr:
    if value in counts:
      counts[value] += 1
    else:
      counts[value] = 1
    if counts[value] <= n:
      result.append(value)
  return result

if __name__ == '__main__':
  print(limit([1, 2, 3, 1, 2, 1, 2, 3], 2))
