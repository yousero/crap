
"""
  Task Tracker
"""

import json
import os
import sys
import datetime
import uuid
import pprint
import fire

path = os.path.dirname(sys.argv[0])
file_path = os.path.join(path, 'tasks.json')

def json_obj():
  j = []
  try:
    j = json.load(open(file_path, 'r', encoding='utf-8'))
  except json.decoder.JSONDecodeError:
    pass
  except FileNotFoundError:
    pass
  return j

def save_obj(j):
  json.dump(j, open(file_path, 'w', encoding='utf-8'))

def add(task_name):
  j = json_obj() 

  _id = j[-1]['id'] + 1 if len(j) else 1
  task = {
    'id': _id,
    'description': task_name,
    'status': 'todo',
    'createdAt': datetime.datetime.now().isoformat(),
    'updatedAt': datetime.datetime.now().isoformat()
  } 

  j.append(task)
  save_obj(j)

  i = len(j)
  return f'Task added successfully (ID: {i})'

def update(_id, task_name):
  j = json_obj() 

  task = j[_id]
  task |= {
    'description': task_name,
    'status': 'todo',
    'updatedAt': datetime.datetime.now().isoformat()
  } 

  j[_id] = task
  
  save_obj(j)

def delete(_id):
  j = json_obj() 
  del j[_id]
  save_obj(j)

def mark_in_progress(_id):
  j = json_obj() 
  j[_id]['status'] = 'in-progress'
  save_obj(j)

def mark_done(_id):
  j = json_obj() 
  j[_id]['status'] = 'done'
  save_obj(j)

def _list(mark=''):
  j = json_obj()
  if mark: j = [x for x in j if x['status'] == mark]
  for x in j:
    pprint.pprint(x, sort_dicts=False)
    print()

if __name__ == '__main__':
  fire.Fire({
    'add': add,
    'update': update,
    'delete': delete,
    'mark-in-progress': mark_in_progress,
    'mark-done': mark_done,
    'list': _list
  })
