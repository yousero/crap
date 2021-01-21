("""
 meta, the bot
""")

import datetime
import textwrap
import argparse
import logging

import yaml
from aiogram import Bot, Dispatcher, executor, types, md

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description='Meta bot')
parser.add_argument('--api-token', '-t', type=str, help='API token')
parser.add_argument('--user-id', '-id', type=str, help='User ID')

args = parser.parse_args()


bot = Bot(token=args.api_token, parse_mode='Markdown')
dp = Dispatcher(bot)

command = ''

@dp.message_handler(user_id=args.user_id, 
  commands=['start', 'help', 'menu', 'welcome'])
async def welcome_message(message: types.Message):
  await message.answer(textwrap.dedent("""
      My name is Theta, and I do a lot of things.

      /date, /time – show current date and time
      /id – send you chat_id
      /meta – unparse metadata of message

      /help – show this message
    """))


@dp.message_handler(user_id=args.user_id, commands=['meta'])
async def meta_message(message: types.Message):
  global command
  command = 'meta'


@dp.message_handler(user_id=args.user_id, 
  commands=['date', 'day', 'time', 'datetime'])
async def day_message(message: types.Message):
  await message.answer(datetime.datetime.now().isoformat())


@dp.message_handler(user_id=args.user_id,
  commands=['id', 'my_id'])
async def id_message(message: types.Message):
  await message.answer(message.chat.id)


@dp.message_handler(user_id=args.user_id)
async def any_message(message: types.Message):
  global command
  if command == 'meta':
    code = f'```\n#{yaml.dump(message.to_python())}\n```'
    await message.answer(code)
  command = ''


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
 
