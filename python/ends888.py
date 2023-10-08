k = []
cases = int(input())
for i in range(cases):
    k.append(input())



def endsInFatLadies(number):
    cube = number ** 3
    cubeString = str(cube)
    cube = int(cubeString[-3:])
    if cube == 888:
        return number ** 3
    else:
        return -10

outs = 0

while len(k) != 0:
    for i in range(cases):
        testedCase = k[0]
        counter = int(testedCase)
        for i in range(int(testedCase) + 1, int(testedCase) + 5000):
            if endsInFatLadies(i) == -10:
                pass
            else:
                print(counter+1)
                del k[0]
                break
            counter += 1