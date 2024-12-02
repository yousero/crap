
"""
  Creates an array of elements split into groups the length of `size`.
"""

def chunk(array, size=1):
  result = []
  while len(array):
    x = []
    for i in range(size):
      if len(array):
        x.append(array.pop(0))
    result.append(x)
  return result

if __name__ == '__main__':
  print(chunk(['a', 'b', 'c', 'd'], 2))
