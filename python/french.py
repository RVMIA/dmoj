tUpper = 0
tLower = 0
sUpper = 0
sLower = 0
cases = int(input())
for i in range(cases):
    line = str(input())
    tUpper += line.count("T") 
    tLower += line.count("t")
    sUpper += line.count("S") 
    sLower += line.count("s")

tcount = tUpper + tLower
scount = sUpper + sLower
if cases != 0:
    if scount >= tcount:
        print("French")
    elif scount < tcount:
        print("English")