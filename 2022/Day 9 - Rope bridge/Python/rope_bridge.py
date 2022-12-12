import math
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def set(self, x, y): 
        self.previous_x, self.previous_y = self.x, self.y
        self.x, self.y = x, y

    def get_tuple(self):
        return (self.x, self.y)
    
class RopeBridge:
    def __init__(self, num_tails=1):
        self.prev_head = None
        self.knots = [Point(0,0)] # default is one head and one tail
        self.num_tails = num_tails # allows us to add a chain of tails
        self.tail_history = [set()] # create a set for the first tail
        self.command_number = 0

    def simulate(self, input:list):
        # iterate through each command
        for i, x in enumerate(input): 
            # process a command for every knot and it's head
            self.process_command(x)
            # self.show_move(x)

    def process_command(self, m:str):
        curr_dir = m[0] # get the direction to move the heazd
        for _ in range(int(m[1])): # repeat the move the specified number of times
            # for each move for the first <num_tails> moves, add a new knot
            if self.command_number < self.num_tails:
                self.knots.append(Point(0,0))
                self.tail_history.append(set())
                self.command_number += 1
                
            if curr_dir == "L": # LEFT
                self.moveHead(-1, 0)
            elif curr_dir == "R": # RIGHT
                self.moveHead(1, 0)
            elif curr_dir == "U": # UP
                self.moveHead(0, 1)
            elif curr_dir == "D": # DOWN
                self.moveHead(0, -1)

   
    def moveHead(self, x:int, y:int):
        head = self.knots[0]
        # Move the head knot
        head.set(head.x + x, head.y + y)
        # move the tails
        self.move_tails()   

    def move_tails(self):
        for i in range(0, len(self.knots) - 1):
            head = self.knots[i]
            tail = self.knots[i+1]
            if not self.touching(tail.get_tuple(), head.get_tuple()):
                if tail.x == head.x and tail.y != head.y:
                    if tail.y < head.y:
                        tail.set(tail.x, tail.y + 1)
                    else:
                        tail.set(tail.x, tail.y - 1)
                elif tail.x != head.x and tail.y == head.y:
                    if tail.x < head.x:
                        tail.set(tail.x + 1, tail.y)
                    else:
                        tail.set(tail.x - 1, tail.y)
                elif tail.x != head.x and tail.y != head.y:
                    if tail.x < head.x and tail.y < head.y:
                        tail.set(tail.x + 1, tail.y + 1)
                    elif tail.x < head.x and tail.y > head.y:
                        tail.set(tail.x + 1, tail.y - 1)
                    elif tail.x > head.x and tail.y > head.y:
                        tail.set(tail.x - 1, tail.y - 1)
                    elif tail.x > head.x and tail.y < head.y:
                        tail.set(tail.x - 1, tail.y + 1)
                  
            self.tail_history[i].add(tail.get_tuple())

    def touching(self, tail, head):
        return math.dist(tail, head) <= 1.42   

    def show_move(self, move):
        print(move)
        for i, x in enumerate(self.knots):
            if i == 0:
                print("H:", x.get_tuple())
            else:
                print(f"{i}: {x.get_tuple()}")

def test():
    input = [x.strip().split(' ') for x in open("../Input/test_input.txt").readlines()]
    rb = RopeBridge()
    rb.simulate(input)
    print(len(rb.tail_history[0]))

def challenge1():
    input = [x.strip().split(' ') for x in open("../Input/day9_input.txt").readlines()]
    rb = RopeBridge()
    rb.simulate(input)
    print(len(rb.tail_history[0]))

def test2():
    num_tails = 9
    input = [x.strip().split(' ') for x in open("../Input/test2_input.txt").readlines()]
    rb = RopeBridge(num_tails)
    rb.simulate(input)
    print(len(rb.tail_history[num_tails - 1]))

def challenge2():
    num_tails = 9
    input = [x.strip().split(' ') for x in open("../Input/day9_input.txt").readlines()]
    rb = RopeBridge(num_tails)
    rb.simulate(input)
    print(len(rb.tail_history[num_tails - 1]))

test()
challenge1() # should be 6236 (13msec)
test2()
challenge2() # should be 2449 (83msec)