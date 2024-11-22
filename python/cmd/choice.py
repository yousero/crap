import random

array = []

while True:
  try:
    line = input()    
  except EOFError:
    break
  if not line.strip():
    break
  array.append(line)

print(random.choice(array))
