import argparse
import os
import re

parser = argparse.ArgumentParser(description='Rename files by regex')
parser.add_argument('regex', type=str,
                    help='patern for renaming files or directories', )
parser.add_argument('replacer', type=str, 
                    help='string what replaced a patern', )
parser.add_argument('path', nargs='?', type=str, default='.',
                    help='path to directory for scaning', )
parser.add_argument('-D', '--include-dirs', default=False, action='store_const',
                    const=True, help='include directory for renaming', )
args = parser.parse_args()

regex = re.compile(args.regex, re.IGNORECASE)

files_by_regex = []
failed_files = []

for root, dirs, files in os.walk(args.path):
  pool = files

  if args.include_dirs:
    pool = dirs + pool

  for name in pool:
    if regex.search(name):
      replace = regex.sub(args.replacer, name)
      files_by_regex.append([root, name, replace])
      print(f'"{name}" -> "{replace}"')

answer = input('\nDo you want to accept this? [y|N] ')

if answer and answer.lower()[0] == 'y':
  for root, file, replace in files_by_regex:
    try:
      os.rename(os.path.join(root, file), os.path.join(root, replace))
    except Exception as e:
      failed_files.append([root, file])

  print(f'\n{len(files_by_regex) - len(failed_files)} files was renamed')

  if failed_files:
    print('\nfailed files:')
  for root, file in failed_files:
    print(os.path.join(root, file))
