sumac1 = int(input())
sumac2 = int(input())
sumac = [sumac1, sumac2]
while sumac[-2] >= sumac[-1]:
    sumac.append(sumac[-2] - sumac[-1])
print(len(sumac))