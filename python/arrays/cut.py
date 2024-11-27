
"""
  Cut elements from array by constraints.
"""

def cut(arr, min_lim=None, max_lim=None, f=None):
  if len(arr) == 0:
    return arr

  if min_lim is None:
    min_lim = min(arr)
  if max_lim is None:
    max_lim = max(arr)
  if f is None:
    f = lambda x: x

  return list(filter(lambda x: (min_lim <= f(x) <= max_lim), arr))
