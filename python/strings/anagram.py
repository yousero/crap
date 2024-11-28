from collections import Counter

def anagram(str1, str2):
  str1 = str1.replace(' ', '').lower()
  str2 = str2.replace(' ', '').lower()
  return Counter(str1) == Counter(str2)

if __name__ == '__main__':
  print(anagram('apple', 'pleap'))  # Output: True
  print(anagram('listen', 'silent'))  # Output: True
  print(anagram('hello', 'world'))    # Output: False
