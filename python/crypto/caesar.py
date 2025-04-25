

def caesar(text, n, abc='abcdefghijklmnopqrstuvwxyz', unknown=''):
  result = ''
  for c in text:
    if c in abc:
      i = abc.index(c)
      c = abc[(i + n) % len(abc)]
    elif unknown:
      c = unknown
    result += c
  return result


if __name__ == '__main__':
  code = caesar('text from blackhole', 3)
  print(code)
  print(caesar(code, -3))
