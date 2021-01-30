## solving for diaphontine equation
## i.e. ax + by = c

def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)

def diophantine(a, b, c):
  assert c % gcd(a, b) == 0
  # return (x, y) such that a * x + b * y = c
  GCD = gcd(a, b)
  
  ## get solution for:  (a/GCD)*x + (b/GCD)*y = 1
  a //= GCD
  b //= GCD
  RHS = 1

  x = 0
  y = 0
  while True:
    LHS = a*x + b*y
    if LHS < RHS:
      if a < b:
        x += 1
      else:
        y += 1
    elif LHS > RHS:
      if a < b:
        x += 1
        y -= 1
      else:
        x -= 1
        y += 1
    else:
      break
  
  coff = c//GCD

  return (x*coff, y*coff)
 

## testing
diophantine(10,6,14)
