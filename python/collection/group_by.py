
"""
  Creates an `dict` composed of keys generated from the results
  of running each element of `collection` thru `f`.
"""

def group_by(array, f=None):
  if f is None: f = lambda x: x
  obj = {}
  for x in set(array):
    key = str(f(x))
    if key in obj:
      obj[key].append(x)
    else:
      obj[key] = [x]
  return obj
  
if __name__ == '__main__':
  import math
  print(group_by([6.1, 4.2, 6.3], math.floor))
  print(group_by(['one', 'two', 'three'], len))
