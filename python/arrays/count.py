
"""
  Count item in array.
"""

def count(arr, item):
  result = 0
  for x in arr:
    if x == item and type(item) == type(x):
      result += 1
  return result

if __name__ == '__main__':
  print(count([False, 1, True, 0, 1, 2, None, 0, 1, 3, 'a'], 1))
