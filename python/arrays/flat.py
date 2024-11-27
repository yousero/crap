
"""
  Returns a flat array. 
"""

from collections.abc import Iterable

def flat(arr):
  result = []
  for x in arr:
    if not isinstance(x, str) and isinstance(x, Iterable):
      result.extend(flat(x))
    else:
      result.append(x)
  return result

if __name__ == '__main__':
  print(flat([1, 2, 3, [4, 5, [6]]]))
