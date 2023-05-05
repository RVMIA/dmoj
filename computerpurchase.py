terms = input()
devices = {}
deviceNames = []
deviceRanks = []


if int(terms) == 1:
    statistics = input().split()
    print(statistics[0])
  
elif int(terms) == 0:
    pass

else:
    for i in range(int(terms)):
            statistics = input().split()

            name = statistics[0]
            ram = int(statistics[1])
            cpu = int(statistics[2])
            space = int(statistics[3])
            computerRank = (int((2*ram) + (3*cpu) + space))

            devices.setdefault(computerRank, name)
            deviceNames.append(name)
            deviceRanks.append(computerRank)

    deviceRanks.sort(reverse=True)
    if deviceRanks[0] == deviceRanks[1]:
        print(sorted(deviceNames[0:1]))
    
    if len(deviceRanks) > 2 and deviceRanks[1] == deviceRanks[2]:
        deviceNames[1:2].sort()
        print(deviceNames[0])
        print(deviceNames[1])

    else:
        print(devices.get(deviceRanks[0]))
        print(devices.get(deviceRanks[1]))