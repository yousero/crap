import math

def octcode_encode(data):
  result = ''
  buf = ''
  for b in bytes(data, encoding='utf-8'):    
    s = ''.join(list(reversed(bin(b)[2:])))
    if len(s) < 8:
      s += '0' * (8 - len(s))
    s = buf + s
    buf = ''
    for i in range(math.ceil(len(s)/3)):
      ch = s[i*3:i*3+3]
      if len(ch) == 3:
        result += oct(int(ch, 2))[2:]
      else:
        buf = ch
  if buf:
    if len(buf) < 3:
      buf += '0' * (3 - len(buf))
    result += oct(int(buf, 2))[2:]
  return result

def octcode_decode(data):
  seq = ''
  for c in data:
    b = bin(int(c, 8))[2:]
    if len(b) < 3:
      b = '0' * (3 - len(b)) + b
    seq += b
  seq = seq.rstrip('0')
  r = [int(''.join(list(reversed(seq[i:i+8]))), 2) 
       for i in range(0, len(seq), 8)]
  return bytes(r).decode('utf-8')

if __name__ == '__main__':
  print(oct_encode('hello from another universe'))
  print(oct_decode('4757325663523116754'))
