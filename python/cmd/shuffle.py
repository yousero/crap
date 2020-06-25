
"""
Shuffle readlines and print them. 
Needs number of strings in first line.
"""

import random


n = int(input())
array = [input() for i in range(n)]

random.shuffle(array)

for string in array:
  print(string)
