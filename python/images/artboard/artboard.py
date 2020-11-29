import json

from PIL import Image


class Artboard:
  """
    Artboard with layers with different format images.

    >>> art = json.load(open('artboard.json'), object_hook=Artboard.object_hook)
    >>> art.render()
    >>> art.image.save('art.png')
  """

  def __init__(self, width=0, height=0, layers=None):
    self.width, self.height = width, height
    self.layers = [] if not layers else layers
    self.image = Image.new('RGB', (width, height))

  @classmethod
  def object_hook(cls, obj):
    if obj['type'] == 'artboard':
      return cls(obj['width'], obj['height'], obj['layers'])
    elif obj['type'] == 'layer':
      return {
        'image': Image.open(obj['file']),
        'xy': obj['xy']
      }

  def render(self):
    self.image = Image.new('RGB', (self.width, self.height))
    for l in self.layers:
      print(l['image'].size)
      self.image.paste(l['image'], l['xy'])

if __name__ == '__main__':
  import doctest
  doctest.testmod()
