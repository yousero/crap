

class Sokoban:
  #  Territory ids
  #  -1      0      1    2     3
  #  player  space  box  wall  storage

  def __init__(self, territory=None):

    self.territory = None
    self.size = None
    self.player = None
    self.boxes = set()
    self.storage =  set()
    self.walls = set()
    self.spaces = 0

    if type(territory) != list:
      raise TypeError('invalid territory argument')
    
    if territory is not None:
      self.territory = territory
      self.update()


  def update(self):
    max_y = len(self.territory)
    max_x = 0

    for y, row in enumerate(self.territory):
      max_x = max(max_x, len(row))
      for x, cell in enumerate(row):
        if self.player is None and cell == -1:
          self.player = (y, x)
        elif cell == 0: self.spaces += 1
        elif cell == 1: self.boxes.add((y, x))
        elif cell == 2: self.walls.add((y, x))
        elif cell == 3: self.storage.add((y, x))

    self.size = (max_y, max_x)


  def map(self):
    h, w = self.size
    m = [[0 for i in range(w)] for j in range(h)]    
    
    for y, x in self.storage: m[y][x] = 3    
    for y, x in self.boxes: m[y][x] = 1
    for y, x in self.walls: m[y][x] = 2

    y, x = self.player
    m[y][x] = -1

    self.territory = m


  def ifinto(self, obj):
    for i, c in enumerate(obj):
      if c < 0 or c >= self.size[i]:
        break
    else:
      return True
    return False


  def move(self, direction):
    x = 0
    y = 0

    if direction == 'up':
      y = -1
    elif direction == 'down':
      y = 1
    elif direction == 'right':
      x = 1
    elif direction == 'left':
      x = -1

    a, b = self.player
    a, b = a + y, b + x
    n = a, b

    if not self.ifinto(n):
      return False
    
    if n in self.boxes:
      box = a + y, b + x
      if not self.ifinto(box):
        return False

      self.boxes.remove(n)
      self.boxes.add(box)

    self.player = a, b


  def print(self):
    print('player:', self.player)
    print('boxes:', self.boxes)

    self.map()

    for r in self.territory:
      print(*[f'[ {x:^3} ]' for x in r])


def main():
  s = Sokoban([
      [0, 0, 0, 0], 
      [0, -1, 3, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 0]
    ])
  
  s.print()

  s.move('down')
  s.move('down')
  s.move('right')
  s.move('up')

  s.print()


if __name__ == '__main__':
  main()
