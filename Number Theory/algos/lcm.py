## Least Common Multiple
def lcm(a, b):
  assert a > 0 and b > 0
  
  assert a+b > 0
  mul = a*b

  while a>0 and b>0:
    if a>=b:
      a %= b
    else:
      b %= a
  
  gcd = max(a,b)
  return mul//gcd

## testing
lcm(8,4)
