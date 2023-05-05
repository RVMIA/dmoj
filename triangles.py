import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

if (A + B + C) != 180:
    print("Error")
elif A == B  == 60:
    print("Equilateral")
elif (A + B + C) == 180 and A != B and B != C and A != C:
    print("Scalene")
else:
    print("Isosceles")