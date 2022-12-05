def challenge1():
    total = 0
    with open("../Input/day4_input.txt") as o:
        for line in o:
            elfA = [int(x) for x in line.strip().split(',')[0].split('-')]
            elfB = [int(x) for x in line.strip().split(',')[1].split('-')]
            if (elfA[0] <= elfB[0] and elfA[1] >= elfB[1]) or (elfB[0] <= elfA[0] and elfB[1] >= elfA[1]):
                total += 1
                print(elfA, elfB, "True")
            else:
                print(elfA, elfB, "False")
        print(total)

def challenge2():
    total = 0
    with open("../Input/day4_input.txt") as o:
        for line in o:
            elfA = [int(x) for x in line.strip().split(',')[0].split('-')]
            elfB = [int(x) for x in line.strip().split(',')[1].split('-')]
            setA = set(range(elfA[0], elfA[1] + 1))
            setB = set(range(elfB[0], elfB[1] + 1))
            print()
            if (len(setA.intersection(setB)) > 0):
                total += 1
                print(elfA, elfB, "True")
            else:
                print(elfA, elfB, "False")
        print(total)

        
# challenge1()
challenge2()