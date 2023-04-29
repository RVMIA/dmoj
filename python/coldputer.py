count = 0
iterations = int(input())
data = input().split()
for i in range(iterations):
        if (int(data.pop(0)) < 0):
            count += 1

print(count)