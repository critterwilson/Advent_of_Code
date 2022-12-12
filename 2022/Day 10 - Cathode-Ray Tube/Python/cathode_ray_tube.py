class Clock:
    def __init__(self) -> None:
        self.register = []

    def cycle(self, input):
        for command in input:
            for word in command:
                if word == "noop" or word == "addx":
                    self.register.append(0)
                else:
                    self.register.append(int(word))

def test(input):
    c = Clock()
    c.cycle(input)
    print(c.register)

def test2(input):
    c = Clock()
    c.cycle(input)
    total = 0
    for x in [20, 60, 100, 140, 180, 220]:
        y = (sum([1] + c.register[0:x])) * x
        print(f"{x}: {y}")
        total += y
    
    print(total)

def challenge1(input):
    c = Clock()
    c.cycle(input)
    total = 0
    for x in [20, 60, 100, 140, 180, 220]:
        y = (sum(c.register[0:x]) + 1) * x
        print(f"{x}: {y}")
        total += y

    print("Total:", total)
def challenge2(input):
    pass

test_input = [x.strip().split(' ') for x in open("../Input/test_input.txt").readlines()]
test2_input = [x.strip().split(' ') for x in open("../Input/test2_input.txt").readlines()]
input = [x.strip().split(' ') for x in open("../Input/day10_input.txt").readlines()]

test(test_input)
test2(test2_input)
# print(challenge1(input))