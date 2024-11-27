
"""
  Sorts text lines from input.
"""

array = []

while True:
  try:
    line = input()
  except EOFError:
    break
  if not line.strip():
    break
  array.append(line)

array.sort()

for string in array:
  print(string)
