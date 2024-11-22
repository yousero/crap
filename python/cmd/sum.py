
s = 0

while True:
  try:
    line = input()
  except EOFError:
    break
  if not line.strip():
    break
  try:
    s += int(line)
  except ValueError:
    break

print(s)
