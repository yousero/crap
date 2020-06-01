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
dirs_by_regex = []

failed_paths = []

for root, dirs, files in os.walk(args.path):
  pool = [(name, False) for name in files]

  if args.include_dirs:
    pool += [(name, True) for name in dirs]

  for name, is_dir in pool:
    match = regex.search(name)

    if match:
      replacer = re.sub(
        r'\$(\d+)',
        lambda m: match.group(int(m.group(1))),
        args.replacer)

      replace = regex.sub(replacer, name)

      if is_dir:
        dirs_by_regex.append([root, name, replace])
      else:
        files_by_regex.append([root, name, replace])

      print(f'"{name}" -> "{replace}"')

answer = input('\nDo you want to accept this? [y|N] ')

if answer and answer.lower()[0] == 'y':
  for root, file, replace in files_by_regex:
    try:
      os.rename(os.path.join(root, file), os.path.join(root, replace))
    except Exception as e:
      failed_paths.append([root, file])

  for root, name, replace in dirs_by_regex:
    try:
      os.rename(os.path.join(root, name), os.path.join(root, replace))
    except Exception as e:
      failed_paths.append([root, name])

  count = len(files_by_regex) + len(dirs_by_regex) - len(failed_paths)
  print(f'\n{count} files was renamed')

  if failed_paths:
    print('\nfailed paths:')
  for root, file in failed_paths:
    print(os.path.join(root, file))
