import math

A = input().split()
B = input().split()
C = input().split()


def distance(point1, point2):
	return math.sqrt((( int(point1[0]) - int(point2[0]) ) ** 2 ) + (( int(point1[1]) - int(point2[1]) ) ** 2 ))

def area(point1, point2, point3):
	S = ((point1 + point2 + point3)/2)
	return math.sqrt(S * (S - point1) * (S - point2) * (S - point3))

AB = distance(A, B)
BC = distance(B, C)
CA = distance(C, A)

Area = area(AB, BC, CA)

print(Area)



    