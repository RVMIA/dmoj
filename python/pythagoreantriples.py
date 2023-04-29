out = []
for i in range(100):
    for j in range(100):
        for k in range(100):
            if i^2 + j^2 == k^2 and i > 0 and j > 0 and k > 0:
                out1 = [i, j, k]
                out.append(out1)
                if len(out) % 1000 == 0:
                    print(out[-1])
print(out)
print(len(out))
