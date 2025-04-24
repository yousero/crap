import psutil
import time
from tabulate import tabulate

def process_list():
  processes = []
  for proc in psutil.process_iter(
      ['pid', 'name', 'memory_info']):
    try:
      processes.append((
        proc.info['pid'],
        proc.info['name'],
        round(proc.info['memory_info'].rss / 1024 / 1024, 2)
      ))
    except (psutil.NoSuchProcess, psutil.AccessDenied):
      pass
  return processes

if __name__ == '__main__':
  processes = process_list()
  processes.sort(key=lambda x: x[2], reverse=True)
  print(tabulate(processes, 
    headers=('PID', 'Name', 'Memory (MB)'), tablefmt='grid')
  )
