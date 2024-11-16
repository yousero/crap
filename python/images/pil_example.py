import sys
import os
from PIL import Image

filename = sys.argv[1]

if os.path.exists(filename):
  image = Image.open(filename)
  image.save('new.jpg', quality=98)
