
"""
  Generate elements of `array` with `value` from 
  `start` up to, but not including, `end`.
"""
def fill_generator(array, value, start=0, end=None):
  result = []
  if end is None: end = len(array)

  for i, x in enumerate(array):
    if start <= i < end:
      x = value
    yield x

if __name__ == '__main__':
  print(list(fill_generator(range(8), 1)))
  print(list(fill_generator([1, 2, 3], 'x')))
