import math
from math import gcd as bltin_gcd

def coprime2(a, b):
    return bltin_gcd(a, b) == 1
n = 1000000
pilist = 100
coprime = 0
cofactor = 0
for i in range(n):
    
    for j in range(n):
        if coprime2(i, j):
            coprime += 1
        else:
            cofactor += 1
        
        if cofactor > 0 and coprime > 0:
            ratio = (cofactor)/(coprime)
            offPi = math.sqrt(6.0/ratio)
            diff = abs(math.pi-offPi)
            if diff < pilist:
                pilist = diff
                print(diff, offPi, (i*j)/float(n^2))
            
    
#print(pilist[-1])

#  Measure-Command { pypy .\randomPi.py | Out-Default }


