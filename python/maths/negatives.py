def negatives(nums):
  """Return the negative numbers in the given list.
  
  >>> negatives([5, -1, -2, 0, 3])
  [-1, -2]
  """

  if any(type(x) not in [int, float] for x in nums):
    raise ValueError('.nums not contained numbers')

  return [num for num in nums if num < 0]

if __name__ == '__main__':
  import doctest
  doctest.testmod()
