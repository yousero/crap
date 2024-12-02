
"""
  Returns the index of the first element specified by the lambda `f`.
"""

def find_index(array, f=None, from_index=0):
  index = None
  if f is None: f = lambda x: x

  for i, x in enumerate(array):
    if f(x): return i

  if index is None:
    raise ValueError('value is not in array')

  return index

if __name__ == '__main__':
  users = [
    { 'user': 'barney',  'active': False },
    { 'user': 'fred',    'active': False },
    { 'user': 'pebbles', 'active': True }
  ]

  print(find_index(users, lambda x: x['user'] == 'barney'))
