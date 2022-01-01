romanNos = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

total = 0
rom = input()
for i in range(1,len(rom)):
    if romanNos[rom[i-1]] < romanNos[rom[i]]:
        total -= romanNos[rom[i-1]]
    else:
        total += romanNos[rom[i-1]]
    
total+=romanNos[rom[-1]]
print(total)
