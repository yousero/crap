
"""
  Creates an array of `array` values not included in the other given arrays.
"""

import copy
from collections.abc import Iterable
from include import include

def difference(array, values, f=None, *args):
  s = set()
  f = lambda x: not include.include(s, x)
  values.extend(args)
  for x in values:
    if not isinstance(x, str) and isinstance(x, Iterable):
      s.update(x)
    else:
      s.add(x)
  return list(filter(f, array))

if __name__ == '__main__':
  print(difference([2, 1], [2, 3]))
