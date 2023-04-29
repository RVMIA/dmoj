points = []
terms = int(input())
for i in range(terms):
    if len(points) < terms:
        points.append(int(input()))
points.sort()
#print(*points, sep='\n')
for i in range(terms):
    print(points.pop(0))
