import requests
import random
import json
from bs4 import BeautifulSoup
from tqdm import tqdm

abc_ru = 'абвгдежзийклмнопрстуфхцчшщэюя'.upper()
words = []

try:
  with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)
except FileNotFoundError:
  pass

base_url = 'https://ozhegov.slovaronline.com'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def upload_words():
  for k,v in enumerate(tqdm([x for x in words if len(x) == 2])):
    response = requests.get(f'{base_url}{v[1]}', headers=headers)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      div = soup.find(class_='blockquote')
      words[k] += (div.get_text(),)
    else:
      break


def upload():
  urls = [f'{base_url}/articles/{c}/page-1' for c in abc_ru]
  
  for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find(class_='articles-link-list')
    words.extend([(x.get_text(), x['href']) for x in div.find_all('a', href=True)])

  upload_words()


def get_random_word():
  if not len(words):
    upload()
  elif not all([len(x) == 3 for x in words]):
    upload_words()
  with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f)
  return random.choice(words)


if __name__ == '__main__':
  random_word = get_random_word()
  print("Случайное слово:", random_word)
