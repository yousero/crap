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

base_url = "https://ozhegov.slovaronline.com"

def upload():
  urls = [f'{base_url}/articles/{c}/page-1' for c in abc_ru]

  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
  
  for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find(class_='articles-link-list')
    words.extend([(x.get_text(), x['href']) for x in div.find_all('a', href=True)])
  
  for k,v in enumerate(tqdm(words)):
    response = requests.get(f'{base_url}{v[1]}', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find(class_='blockquote')
    words[k] += (div.get_text(),)


def get_random_word():
  if not len(words):
    upload()
    with open('words.json', 'w', encoding='utf-8') as f:
      json.dump(words, f)
  return random.choice(words)


if __name__ == '__main__':
  random_word = get_random_word()
  print("Случайное слово:", random_word)
