import math

class Monkey:
    def __init__(self, details):
        self.items = [int(x) for x in details[0].split(", ")] 
        self.operation = details[1].replace('old', 'monkey.items[i]').replace("new", "monkey.items[i]")
        self.test = f"monkey.items[i] % {details[2].split()[-1]} == 0"
        self.true = int(details[3].split()[-1])
        self.false = int(details[4].split()[-1])
        self.inspections = 0
    
    def __str__(self):
        return f"Monkey:\n  items: {', '.join([str(x) for x in self.items])}\n  Operation: {self.operation}\n  Test: {self.test}\n    If true: {self.true}\n    If false: {self.false}\n  Inspections: {self.inspections}"

class MonkeyBusiness:
    def __init__(self, input) -> None:
        self.monkeys = self.process_input(input)
        for monkey in self.monkeys:
            print(monkey)
    
    def process_input(self, input): 
        monkeys = []
        for monkey in input:
            details = [x.split(':')[-1].strip() for x in monkey.split("\n")][1::]
            monkeys.append(Monkey(details))
        return monkeys         

    def monkey_in_the_middle(self, rounds):
        for _ in range(rounds):
            for monkey in self.monkeys:
                for i in range(len(monkey.items)):
                    monkey.inspections += 1
                    # process item
                    print('Before Operation: ', monkey.items[i])
                    exec(monkey.operation)
                    print('After Operation: ', monkey.items[i])
                    monkey.items[i] = self.manage_worry()
                    print('After Boredom: ', monkey.items[i])
                    if eval(monkey.test):
                        print(f"Send to {monkey.true}")
                        self.monkeys[monkey.true].items.append(monkey.items[i])
                    else:
                        print(f"Send to {monkey.false}")
                        self.monkeys[monkey.false].items.append(monkey.items[i])
                monkey.items = [] 

        for monkey in self.monkeys:
            print(monkey)

            



def test():
    s = open("../Input/test_input.txt").read().split("\n\n")
    mb = MonkeyBusiness(s)
    print('-------------------------------------------')
    mb.monkey_in_the_middle(20)


def challenge1():
    s = open("../Input/day11_input.txt").read().split("\n\n")
    mb = MonkeyBusiness(s)
    print('-------------------------------------------')
    mb.monkey_in_the_middle(20)
    l = [monkey.inspections for monkey in mb.monkeys]
    l.sort()
    print(math.prod(l[-2::]))

def challenge2():
    pass

challenge1()