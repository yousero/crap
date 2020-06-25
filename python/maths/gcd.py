

def gcd(x, y):
    """
    >>> gcd(24, 40)
    8
    """
    while y:  # --> when y=0 then loop will terminate and return x as final GCD.
        x, y = y, x % y
    return x


if __name__ == '__main__':  
  import doctest
  doctest.testmod()
