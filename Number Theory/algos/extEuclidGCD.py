# Extended Euclid's Algorithm
def extended_gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0

  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd(b, a % b)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

# testing
extended_gcd(10,6)
extended_gcd(7,5)
extended_gcd(391,299)
extended_gcd(239,201)
