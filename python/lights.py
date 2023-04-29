row = []
for i in range(100 + 1):
    row.append(i)
    if i % 10 == 0:
        print("\u0332".join("test"))
        row = []
