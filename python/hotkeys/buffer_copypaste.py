import keyboard
import pyperclip

l = []

def add_paste():
  l.append(pyperclip.paste())

keyboard.add_hotkey('ctrl+c', add_paste)
keyboard.wait('esc')

with open('buffer.txt', 'a', encoding='utf-8') as f:
  f.write('\n'.join(l))
