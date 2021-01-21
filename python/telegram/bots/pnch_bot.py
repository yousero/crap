("""
  Kicker, kick bad guy from Telegram Chat.
""")

import datetime
import textwrap
import argparse
import logging

from aiogram import Bot, Dispatcher, executor, types, md
from aiogram.types import ChatType, ForceReply
from aiogram.types.message_entity import MessageEntityType

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description='Punch bot')
parser.add_argument('--api-token', '-t', type=str, help='API token')

args = parser.parse_args()

bot = Bot(token=args.api_token, parse_mode='MarkdownV2')
dp = Dispatcher(bot)

@dp.message_handler(chat_type=ChatType.PRIVATE, 
  commands=['start', 'help', 'menu', 'welcome'])
async def welcome_message(message: types.Message):
  await message.answer(textwrap.dedent("""
      I am @pnch\_BoT and yours to serve\.

      /kick, /remove – delete someone from chat
      /punch, /ban – disable user access
      /suicide, /leave – remove me from chat

      /help – show this message
    """))


@dp.message_handler(is_chat_admin=True,
  chat_type=[ChatType.GROUP, ChatType.SUPERGROUP],
  commands=['kick', 'remove'])
async def kick_message(message: types.Message):
  users = [
     en.user for en in message.entities 
     if en.type in [MessageEntityType.MENTION, MessageEntityType.TEXT_MENTION]]

  if users:
    for u in users:
      await bot.kick_chat_member(message.chat.id, u.id)
  else:
    await message.reply('send me chat members', reply_markup=ForceReply.create(True))


@dp.message_handler(is_chat_admin=True,
  chat_type=[ChatType.GROUP, ChatType.SUPERGROUP],
  commands=['punch', 'ban'])
async def punch_message(message: types.Message):
  until = datetime.datetime.now() + datetime.timedelta(1000)
  users = [
     en.user for en in message.entities 
     if en.type in [MessageEntityType.MENTION, MessageEntityType.TEXT_MENTION]]

  if users:
    for u in users:
      await bot.kick_chat_member(message.chat.id, u.id, until)
  else:
    await message.reply('send me chat members', reply_markup=ForceReply.create(True))


@dp.message_handler(is_chat_admin=True,
  chat_type=[ChatType.GROUP, ChatType.SUPERGROUP],
  commands=['roulette', 'random'])
async def roulette_message(message: types.Message):
  await message.answer('doesn\'t work')


@dp.message_handler(is_chat_admin=True,
  chat_type=[ChatType.GROUP, ChatType.SUPERGROUP],
  commands=['wipe', 'clean'])
async def wipe_message(message: types.Message):
  await message.answer('doesn\'t work')


@dp.message_handler(is_chat_admin=True,
  chat_type=[ChatType.GROUP, ChatType.SUPERGROUP],
  commands=['suicide', 'leave'])
async def suicide_message(message: types.Message):
  bot.leave_chat(message.chat.id)


@dp.message_handler(is_chat_admin=True,
  chat_type=[ChatType.GROUP, ChatType.SUPERGROUP])
async def any_message(message: types.Message):
  users = [
     en.user for en in message.entities 
     if en.type in [MessageEntityType.MENTION, MessageEntityType.TEXT_MENTION]]

  if users:
    for u in users:
      await bot.kick_chat_member(message.chat.id, u.id)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
 
