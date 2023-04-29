def size(s):
    return (((s+2)*3)+16)


s = int(input())
stretch = int(input())

if size(s) < stretch:
    print("Yes it fits!")
else:
    print("No, it's too small :(")
