"""
  Finds the most frequent items.
"""

from include import include

def frequent(arr):
  values = {}
  result = []

  for i in arr:
    if include(values, i):
      values[i] += 1
    else:
      values[i] = 1

  f_val = max(values.values())
      
  for i in values.keys():
    if values[i] == f_val:
      result.append(i)
    else:
      continue

  return result

if __name__ == '__main__':
  print(frequent([1, 2, 3, 1, 2, 1, 2, 3]))
