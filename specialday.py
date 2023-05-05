import sys

month = int(sys.stdin.readline())
day = int(sys.stdin.readline())

if month == 2 and day == 18:
    print("Special")

elif month == 2 and day != 18:
    if day > 18:
        print("After")
    else:
        print("Before")
else:
    if month > 2:
        print("After")
    else:
        print("Before")    