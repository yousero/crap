N = 8
END = 10
COLUMNS = 3

buff = []
buff_size = 0

def bprint(string='\n'):
  global buff_size, buff

  for _string in string.split('\n'): 
    if buff_size > END - 1:
      buff[buff_size % END] += '\t' + _string
    else:
      buff.append(_string)
    
    buff_size += 1
    
    if buff_size == END * COLUMNS:
      print('\n'.join(buff))
      print()
      buff.clear()
      buff_size = 0


def xor(AL):
  BL = ''

  for i in range(N):
    BL += str(int(AL[i % N - 1]) ^ int(AL[i+1 % N - 1]))

  return BL

def to_k(string):
  A = []
  c = 0
  ch = ''

  for i, x in enumerate(string):
   
    if ch != '' and x == ch:
      c += 1
    else:
      if ch != '':
        A.append(c)
      ch = x
      c = 1
    
    if i+1 == len(string):
      if A and x == string[0]:
        A[0] += c
      else:
        A.append(c)

  return '_'.join(map(str, sorted(A)))

def hole(AL='01010110'):
  for i in range(END):
    bprint(f'{i:3}: {AL}')
    AL = xor(AL)

print()


L = []
M = {}

LK = []
MK = {}

for n in range(2**N):
  S = f'{n:08b}'
  
  if S in L:
    continue

  L.append(S)
  M[S] = xor(S)
  
  LK.append(to_k(S))
  MK[to_k(S)] = to_k(xor(S))


UL = []

for S in L:
  shift = S.rfind('1') + 1
  if shift > 0:
    S = S[shift:] + S[:shift]
  
  IS = f'{int(S, 2) ^ (2 ** N - 1):08b}'
  
  shift = IS.rfind('1') + 1
  if shift > 0:
    IS = IS[shift:] + IS[:shift]

  RIS = ''.join(reversed(IS))

  shift = RIS.rfind('1') + 1
  if shift > 0:
    RIS = RIS[shift:] + RIS[:shift]

  RS = ''.join(reversed(S))

  shift = RS.rfind('1') + 1
  if shift > 0:
    RS = RS[shift:] + RS[:shift]

  if RS not in UL and S not in UL and RIS not in UL and IS not in UL:
    UL.append(S)
 
def to_s(keys):
  sym = 0
  keys = list(map(int, keys.split('_')))
  for i, k in enumerate(keys):
    keys[i] = str(sym) * k
    sym ^= 1

  return ''.join(keys)

ULL = [x for x in UL if x not in list(M.values())]

UK = [x for x in set(LK) if x not in list(MK.values())]

UK = [to_s(x) for x in UK]

print(f'count UK={len(UK)}')
print(UK)

#print(f'count {len(ULL)}, [{", ".join([str(int(x, 2)) for x in ULL])}]')
#print()

for i in UK:
  hole(i)

if buff:
  print('\n'.join(buff))
  print()

