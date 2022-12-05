def alphabetEncoding(char: str) -> int:
    assert(len(char) == 1)
    encodingDict = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
                    "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20,
                    "u":21, "v":22, "w":23, "x":24, "y":25, "z":26,
                    "A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36,
                    "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46,
                    "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52
                    } 
    return encodingDict[char]

def createSet(s: str) -> set: 
    return set(s)

def challenge1():
    total = 0
    with open("../Input/day3_input.txt") as o:
        for line in o:
            x = line.strip()
            first_rucksack = createSet(x[0:len(x)//2])
            second_rucksack = createSet(x[len(x)//2:len(x)])
            intersection = first_rucksack.intersection(second_rucksack)
            total += alphabetEncoding(intersection.pop())
    print(total)


def challenge2():
    total = 0
    l = [set() for _ in range(3)]
    with open("../Input/day3_input.txt") as o:
        for i,x in enumerate(o):
            l[(i + 1) % 3] = set(x.strip())
            if (i + 1) % 3 == 0:
                intersection = l[0].intersection(l[1]).intersection(l[2])
                total += alphabetEncoding(intersection.pop())
    print(total)
                

        

challenge1()
challenge2()