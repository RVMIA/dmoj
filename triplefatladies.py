cases = int(input())
k = int(input())
out = k
def endsInFatLadies(number):
    cube = number ** 3
    while cube >= 1000:
        cube -= 1000
    return cube


while cases != -100:
    if endsInFatLadies(out) == 888:
        print(out)
        cases = -100
    else:
        out += 1

