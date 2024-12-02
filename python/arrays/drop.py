
"""
  Creates a slice of `array` with n elements dropped from the beginning.
"""

def drop(array, f=None):
  result = []
  if f is None: f = 1

  if type(f) == int:
    result = list(array)[f:]
  else:
    w = True
    for x in array:
      if w and f(x):
        continue
      else:
        w = False
      result.append(x)

  T = type(array)
  return T(result)

if __name__ == '__main__':
  print(drop([1, 2, 3]))
  print(drop((4, 5, 6), 2))
  print(drop([1, 2, 3, 0, 5, 6], lambda x: x))
