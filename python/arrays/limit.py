
"""
  Limit array elements by number of occurrences.
"""

from include import include

def limit(arr, n):
  counts = {}
  result = []
  for value in arr:
    if include(counts, item):
      counts[value] += 1
    else:
      counts[value] = 1
    if counts[value] <= n:
      result.append(value)
  return result

if __name__ == '__main__':
  print(limit([1, 2, 3, 1, 2, 1, 2, 3], 2))
