
"""
Output random line from input text
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

print(random.choice(array))
