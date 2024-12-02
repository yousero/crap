
"""
  Determines if a string is an anagram.
"""

import re
from collections import Counter

def anagram(str1, str2):
  str1 = re.sub(r'\s+', '', str1).lower()
  str2 = re.sub(r'\s+', '', str2).lower()
  return Counter(str1) == Counter(str2)

if __name__ == '__main__':
  print(anagram('apple', 'pleap'))  # Output: True
  print(anagram('listen', 'silent'))  # Output: True
  print(anagram('hello', 'world'))    # Output: False
