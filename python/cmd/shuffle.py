
"""
  Shuffle text lines and output them.
"""

import random

array = []
x = True

while x:
  x = False
  try:
    line = input()
  except EOFError:
    break
  if line.strip():
    array.append(line)  
    x = True

random.shuffle(array)

for string in array:
  print(string)
