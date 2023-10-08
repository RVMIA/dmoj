import math
times = 0
a = int(input())
result = math.factorial(a)
resStr = str(result)
for i in range(len(resStr)):
    if (resStr[i] == '0'):
        times += 1
#print(str(times))
print(result)