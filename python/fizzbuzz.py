inputs = input().split()
X = int(inputs[0])
Y = int(inputs[1])
N = int(inputs[2])

for i in range(N + 1):
    if i != 0:
        if i % X == 0 and i % Y == 0:
            print("FizzBuzz")
        elif i % X == 0:
            print("Fizz")
        elif i % Y == 0:
            print("Buzz")
        else:
            print(i)