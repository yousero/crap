
"""
  Returns the first element specified by the lambda `f`.
"""

def find(array, f=None, from_index=0):
  if f is None: f = lambda x: x
  for i, x in enumerate(array[from_index:]):
    if f(x): return x

if __name__ == '__main__':
  users = [
    { 'user': 'barney',  'age': 36, 'active': True },
    { 'user': 'fred',    'age': 40, 'active': False },
    { 'user': 'pebbles', 'age': 1,  'active': True }
  ]

  print(find(users, lambda x: x['age'] < 40))
