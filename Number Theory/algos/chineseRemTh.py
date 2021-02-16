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

def chineseRem(a,b):
  (r,x,y) = extended_gcd(a, b)
  
  if r == 1:
    (ra, rb) = eval(input("enter the pair (ra, rb): "))
    n = ra*b*y + rb*a*x
    return n
    

# testing
chineseRem(10,6)
