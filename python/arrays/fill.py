
"""
  Fills elements of `array` with `value` from 
  `start` up to, but not including, `end`.
"""

def fill(array, value, start=0, end=None):
  result = []
  if end is None: end = len(array)

  for i, x in enumerate(array):
    if start <= i < end:
      x = value
    result.append(x)

  T = type(array)
  if T not in [list, tuple, set]:
    return result
  return T(result)

if __name__ == '__main__':
  print(fill(range(8), 1))
  print(fill([1, 2, 3], 'a'))
  print(fill([4, 6, 8, 10], '*', 1, 3))
