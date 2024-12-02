
"""
  Creates a new array concatenating `array`
  with any additional arrays and/or values.
"""

import copy
from collections.abc import Iterable

def concat(array, *values):
  result = copy.copy(array)
  for x in values:
    if not isinstance(x, str) and isinstance(x, Iterable):
      result.extend(x)
    else:
      result.append(x)
  return result

if __name__ == '__main__':
  print(concat([1], 2, [3], [[4]]))
