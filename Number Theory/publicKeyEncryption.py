p = 11
g = 2

a = 5
b = 7


# Public key of Alice
A = pow(g,a)%p

# Public key of Bob
B = pow(g,b)%p

# Secreat key i.e. Common for both
Common = pow(g,a*b)%p

print("Public key of Alice: {} \nPublic key of Bob: {} \nSecreat key i.e. Common for both: {}".format(A, B, Common))
