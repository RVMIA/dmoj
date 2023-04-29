side, radius = input().split()

def square(sideLength):
    return sideLength ** 2

def circle(radiusLength):
    return (radiusLength ** 2) * (355/113)

if (square(int(side))) > (circle(int(radius))):
    print('SQUARE')
else:
    print('CIRCLE')