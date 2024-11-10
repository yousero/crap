import keyboard
import pyperclip
from random_word import RandomWords

rw = RandomWords()

def new_word():
  word = rw.get_random_word()
  print('new word:', word)
  pyperclip.copy(word)
  keyboard.write(word)

keyboard.add_hotkey('ctrl+g', new_word, suppress=True, trigger_on_release=True)
keyboard.wait('esc')
