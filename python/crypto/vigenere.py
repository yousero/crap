
def vigenere_encode(text, key, abc='abcdefghijklmnopqrstuvwxyz'):
  result = ''
  for i, c in enumerate(text):
    if c in abc:
      k = abc.index(list(key)[i % len(key)])
      c = abc[(abc.index(c) + k) % len(abc)]
    result += c
  return result


def vigenere_decode(text, key, abc='abcdefghijklmnopqrstuvwxyz'):
  result = ''
  for i, c in enumerate(text):
    if c in abc:
      k = abc.index(list(key)[i % len(key)])
      c = abc[(abc.index(c) - k) % len(abc)]
    result += c
  return result


if __name__ == '__main__':
  code = vigenere_encode('text from blackhole', 'yellowbanana')
  print(code)
  print(vigenere_decode(code, 'yellowbanana'))
