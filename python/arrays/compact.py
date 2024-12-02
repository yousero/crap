
"""
  Creates an array with all falsey values removed.
"""

def compact(array):
  falseys = ['', None, False, 0, {}, [], (,)]
  return [x for x in array if x not in falseys]

if __name__ == '__main__':
  print(compact([0, 1, False, None, 2, '', 3, [], 4, 5]))
