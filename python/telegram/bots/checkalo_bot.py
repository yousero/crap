"""
This is a to-do list bot.
It saves your to-do list.

TODO:
  inline buttons
  .txt database
  number of tasks
  search
  tags
"""

import textwrap
import logging

from aiogram import Bot, Dispatcher, executor, types, md

API_TOKEN = '123123123:AAAAAAAAAAAAAAAAAAAAAAAAAAA' # TODO: parse from argv

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode='MarkdownV2')
dp = Dispatcher(bot)


task_list = []
scheduler = []

def detect_time(text): # TODO: find library
  pass


@dp.message_handler(commands=['start', 'help', 'menu'])
async def welcome_message(message: types.Message):
  await message.answer(textwrap.dedent("""
      I can put your things in order of alphabet. 
      Send your tasks to me, please. 
      Or use commands below.

      /tasks - your to-do list

      /add - create new task
      /del - delete existing task
      /edit - fix mistakes in task

      /help - show this message
    """))


@dp.message_handler(commands=['tasks', 'todo', 'list'])
async def todo_message(message: types.Message):
  answer = '\n'.join(f'☐ — «{md.italic(x)}»' for x in task_list)
  if answer:
    await message.answer(answer)
  else:
    await message.answer("your task list is empty")


@dp.message_handler(commands=['add', 'add_task'])
async def add_message(message: types.Message):
  if message.text.find(' ') == -1:
    await message.answer("send your task")
  else:
    task_list.append(message.text[message.text.find(' ') + 1:])
    await message.answer("task added")


@dp.message_handler()
async def any_message(message: types.Message):
  task_list.append(message.text)
  await message.answer("task added")


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
