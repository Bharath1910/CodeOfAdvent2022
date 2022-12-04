with open("Dec 4/input.txt") as f:
    score = 0
    data = f.read().splitlines()
    
    for i in data:
        seperatedTestCases = i.split(",")

        firstRange = [int(i) for i in seperatedTestCases[0].split("-")]
        secondRange = [int(i) for i in seperatedTestCases[1].split("-")]

        firstSetRange = set(range(firstRange[0], firstRange[1] + 1))
        secondSetRange = set(range(secondRange[0], secondRange[1] + 1))

        if firstSetRange.intersection(secondSetRange) == firstSetRange or firstSetRange.intersection(secondSetRange) == secondSetRange:
            score += 1

print(score)
     
        