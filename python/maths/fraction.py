from gcd import gcd


class Fraction:
  """
    ratio like one divide by four
  
  >>> fr = Fraction(2, 8)
  >>> fr
  Fraction(2, 8)
  >>> fr.optimize()
  2
  >>> fr
  Fraction(1, 4)
  >>> fr.calc()
  0.25
  """

  def __init__(self, a, divisor):
    if type(a) != int:
      raise TypeError('.a has wrong type')

    if type(divisor) != int:
      raise TypeError('.divisor has wrong type')

    self.a = a
    self.divisor = divisor
  
  def __add__(self, other):
    a = self.a * other.divisor + other.a * self.divisor
    divisor = self.divisor * other.divisor

    return Fraction(a, divisor)
  
  def __sub__(self, other):
    a = self.a * other.divisor - other.a * self.divisor
    divisor = self.divisor * other.divisor

    return Fraction(a, divisor)
  
  def __mul__(self, other):
    a = self.a * other.a
    divisor = self.divisor * other.divisor

    return Fraction(a, divisor)

  def __div__(self, other):
    a = self.a * other.divisor
    divisor = self.divisor * other.a

    return Fraction(a, divisor)

  def __str__(self):
    return f'Fraction({self.a}, {self.divisor})'

  def __repr__(self):
    return str(self)

  def calc(self):
    return self.a / self.divisor

  def optimize(self):
    _gcd = gcd(self.a, self.divisor)

    if _gcd > 1:
      self.a //= _gcd
      self.divisor //= _gcd

      return _gcd


if __name__ == '__main__':  
  import doctest
  doctest.testmod()
