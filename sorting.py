
points = []
terms = int(input())
for i in range(terms):
    points.append(input())
points.sort()
#print(*points, sep='\n')
for i in range(terms):
    print(points.pop(0))