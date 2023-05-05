## T = N + 1
## 2 ABC
## 3 DEF
## 4 GHI
## 5 JKL
## 6 MNO
## 7 PQRS
## 8 TUV
## 9 WXYZ
letters = input()
time = 0
for i in range(len(letters)):
    letter = letters[i]
    if letter == "A" or letter == "B" or letter == "C":
        number = 2
    elif letter == "D" or letter == "E" or letter == "F":
        number = 3
    elif letter == "G" or letter == "H" or letter == "I":
        number = 4
    elif letter == "J" or letter == "K" or letter == "L":
        number = 5
    elif letter == "M" or letter == "N" or letter == "O":
        number = 6
    elif letter == "P" or letter == "Q" or letter == "R" or letter == "S":
        number = 7
    elif letter == "T" or letter == "U" or letter == "V":
        number = 8
    elif letter == "W" or letter == "X" or letter == "Y" or letter == "Z":
        number = 9
    time += number + 1
print(time)
