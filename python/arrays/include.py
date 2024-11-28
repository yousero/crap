
"""
  Checks inclusion.
"""

def include(arr, item):
  for x in arr:
    if x == item and type(item) == type(x):
      return True
  return False

if __name__ == '__main__':
  print(include([False, 1, True, 0, 1, 2, None, 0, 1, 3, 'a'], True))
