
"""
  Move all elements of the selected item to the end of the array.
"""

def move_to_end(arr, item):
  result = []
  count = 0

  for x in arr:
    if x == item:
      count += 1
    else:
      result.append(x)

  result.extend([item] * count)
  return result

if __name__ == '__main__':
  print(move_to_end([False, 1, 0, 1, 2, 0, 1, 3, "a"], 0))
