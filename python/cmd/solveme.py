import random


def task():
  a, b = random.randint(1, 99), random.randint(1, 99)
  question = f'{a} * {b}?'
  answer = a * b
  return question, answer


if __name__ == '__main__':
  while True:
    question, answer = task()
    print(question)
    n = int(input('> '))
    if n != answer:
      print(f'wrong! answer is {answer}.')
    else:
      print('correct.')
