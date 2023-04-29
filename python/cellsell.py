day = int(input())
eve = int(input())
wkd = int(input())
# Plan A
dayCost = 0
if day > 100:
    dayCost = 25*(day-100)
eveCost = eve*15
wkdCost = wkd*20
planA = dayCost + eveCost + wkdCost

# Plan B
dayCost = 0
if day > 250:
    dayCost = 45*(day-250)
eveCost = 35*eve
wkdCost = 25*wkd
planB = dayCost + eveCost + wkdCost

print("Plan A costs " + str(planA)[:2]+"."+str(planA)[2:])
print("Plan B costs " + str(planB)[:2]+"."+str(planB)[2:])
if planA == planB:
    print("Plan A and B are the same price.")
elif planA < planB:
    print("Plan A is cheapest.")
elif planA > planB:
    print("Plan B is cheapest.")
