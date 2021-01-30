## gives 'x' after Modular Division (given three integers a, b, n)
## such that: gcd(a,n) = 1 and n > 1
## b/a = x (mod n)   i.e.  b = ax (mod n)

## to fing GCD of 2 numbers
def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)

## to return value of x (after modular devision)
def divide(a, b, n):
  assert n > 1 and a > 0 and gcd(a, n) == 1
  
  # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
  if b == 0:
    x = 0
  else:
    x = 0
    while (a*x)%n != b:
      x += 1
  
  return x


## testing
divide(3,1,4)
