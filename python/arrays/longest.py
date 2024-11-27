
"""
  Returns the longest sequence in an array.
"""

def longest(arr):
  if len(arr) == 0:
    return None

  result = arr[0]
  pre = None
  count = 1
  m = 0

  for x in arr:
    if pre is not None:
      if pre == x:
        count += 1
      else:
        if count > m:
          m = count
          result = pre
        count = 1
    pre = x
  if count > m:
    result = pre

  return result

if __name__ == '__main__':
  print(longest([1, 1, 1, 2, 2, 4, 5, 6, 6, 7, 7, 7, 7]))
