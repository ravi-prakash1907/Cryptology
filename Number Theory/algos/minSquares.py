'''
Given an n x m grid (where n,m are integers), arrange it with the minimal number of same size squares.
Clearly, it can always be tiled with nm squares of size 1 x 1, but it is not always optimal. 

The objective it to find the minimal number of squares, For example:
a 6 x 10 grid can be arranged by 15 squares of size 2 x 2.
'''

def squares(n, m):
    mul = n*m
    
    while n > 0 and m > 0:
        if n >= m:
            n %= m
        else:
            m %= n
    return mul // (max(n,m)*max(n,m))

## testing
squares(10,6)
