
"""
  Creates an array of unique values that are included in all given arrays.
"""

def intersection(*arrays):
  counts = {}
  for arr in arrays:
    for x in set(arr):
      key = str(hash(str(x) + ' ' + type(x).__name__))
      if key in counts:
        counts[key] += 1
      else:
        counts[key] = 1
  return [v for k, v in counts.items() if v == len(arrays)]
  
if __name__ == '__main__':
  print(intersection([2, 1], [2, 3]))
  print(intersection([2, '1'], ['2', 3]))
