import os

def print_tables(tables, width=None, spaces=3, index_width=3):
  if width is None:
    width = os.get_terminal_size().columns
  space = ' ' * spaces
  lines = []

  if index_width <= 0:
    index_width = -1
  
  tables.sort(key=lambda t: max(len(t), max([len(r) for r in t])), reverse=True)

  for table in tables:
    max_length = max([len(x) for x in table])
    table_len = len(table)
    cursor = 0

    max_width = width
    _count = 0
        
    for i, line in enumerate(lines):  # search free block for table
      line_len = len(line) + max_length + spaces + index_width + 1
      if line_len > width or line_len != max_width:
        _count = 1
        max_width = line_len
        cursor = i
      else:
        _count += 1
      
      if _count >= table_len:
        if not cursor or _count > table_len:
          break
    else:
      cursor = len(lines)

    if cursor:  # print empty line
      line = ' ' * max_length
      try:
        lines[cursor] += line
      except IndexError:
        lines.append(line)
      cursor += 1

    for i, row in enumerate(table):
      if index_width <= 0:
        line = f'{space}{row:{max_length}}'
      else:
        line = f'{space}{i: {index_width}}:{row:{max_length}}'

      try:
        lines[cursor + i] += line
      except IndexError:
        lines.append(line)

  print()
  for row in lines:
    print(row)
  print()


if __name__ == '__main__':
  A = [
    '123123123',
    '66669999',
    '0xffffff',
    'VVVVVVVV',
    'QWEQWEASDASD',
  ]

  B = [
    'OOOOOOOOOO',
    'AAAAAAAAAA',
    'AHAHAHAHAHA',
  ]

  C = [
    'XXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'WWWWWWWWW',
    '0000000000000000',
    '3.1415926',
    '0.618033988749895',
    '0.8660254037844386',
    '1.322875644432295',
  ]

  print_tables([A, B, C])


