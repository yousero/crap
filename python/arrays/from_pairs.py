
"""
  Returns an dict composed from key-value pairs.
"""

def from_pairs(array):
  return {k: v for k, v in array}
  
if __name__ == '__main__':
  print(from_pairs([['a', 1], ['b', 2]]))
