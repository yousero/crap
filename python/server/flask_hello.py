
"""
  Flask Hello World
"""

import click
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return '<h1>Hello, World!</h1>'


@app.route('/hi')
@app.route('/hello')
def say_hello():
  return '<h1>Hello, Flask!</h1>'


@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
  return '<h1>Hello, %s!</h1>' % name


@app.cli.command()
def hello():
  """Just say hello."""
  click.echo('Hello, Human!')
