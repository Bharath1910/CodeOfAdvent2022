stacks = [
    list("RGHQSBTN"),
    list("HSFDPZJ"),
    list("ZHV"),
    list("MZJFGH"),
    list("TZCDLMSR"),
    list("MTWVHZJ"),
    list("TFPLZ"),
    list("QVWS"),
    list("WHLMTDNC")
]

with open("Dec 5/input.txt", 'r') as f:
    for i in f:
        if not i.startswith("move"):
            continue
        
        _, numberOfCrates, _, fromStackPosition, _, toStackPosition = i.split()
        numberOfCrates, fromStackPosition, toStackPosition = int(numberOfCrates), int(fromStackPosition), int(toStackPosition)

        for j in range(numberOfCrates):
            popedCrate = stacks[fromStackPosition - 1].pop()
            stacks[toStackPosition - 1].append(popedCrate)
        
for i in stacks:
    print(i[-1], end="")