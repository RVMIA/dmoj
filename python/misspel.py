count = 0
wordList = []
terms = int(input())
for i in range(terms):
    wordData = input()
    letter = int(wordData[0])
    word = str(wordData[2:])
    count += 1
    if letter == 0:
        print(str(count) + " " + word)
    else: 
        print(str(count) + " " + word[:letter - 1] + word[letter:])