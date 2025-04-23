import os
import argparse

parser = argparse.ArgumentParser(description='tree')
parser.add_argument('path', nargs='?', type=str, default='.',
                    help='path to directory for walk', )
args = parser.parse_args()

prefix = ''

for root, dirs, files in os.walk(args.path):
  level = root.replace(args.path, '').count(os.sep)
  indent = ' ' * 4 * level
  print(f"{indent}{os.path.basename(root)}/")
  sub_indent = ' ' * 4 * (level + 1)
  for f in files:
    print(f"{sub_indent}{f}")
