cases = int(input())
answers = []
for i in range(cases):
    pair = input().split()
    a = pair[0]
    b = pair[1]
    if a[-2:] == '17' or b[-2:] == '17':
        answers.append("NO")
    elif a[-2:] == '11' and b[-1] == '7':
        answers.append("YES")
    elif b[-2:] == '11' and a[-1] == '7':
        answers.append("YES")
    else:
        answers.append("NO")

for i in range(cases):
    print(answers.pop(0))
