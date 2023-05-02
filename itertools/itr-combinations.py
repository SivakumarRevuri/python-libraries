# HACK 2
from itertools import combinations

word, size = input().split(' ')

for i in range(1, int(size)+1):
    possibilities = list(combinations(sorted(word), i))
    for i in possibilities:
        print(''.join(i))
        
"""
OUTPUT:
A
C
H
K
AC
AH
AK
CH
CK
HK
"""