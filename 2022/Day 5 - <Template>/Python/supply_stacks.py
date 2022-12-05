class CrateMover9000(object):
    def __init__(self, board:list, moves:list):
        self.board=board
        self.moves=moves

    def move(self, count:int, fro:int, to:int):
        for _ in range(count):
            self.board[to - 1].append(self.board[fro - 1].pop())

    def parse_move(self, line:str):
        l = line.split(' ')
        return int(l[1]), int(l[3]), int(l[5])

    def simulate_moves(self):
        for move in self.moves:
            count, fro, to = self.parse_move(move)
            self.move(count, fro, to)

class CrateMover9001(object):
    def __init__(self, board:list, moves:list):
        self.board=board
        self.moves=moves

    def move(self, count:int, fro:int, to:int):
        temp = []
        for _ in range(count):
            temp.append(self.board[fro - 1].pop())
        for _ in range(count):
            self.board[to - 1].append(temp.pop())

    def parse_move(self, line:str):
        l = line.split(' ')
        return int(l[1]), int(l[3]), int(l[5])

    def simulate_moves(self):
        for move in self.moves:
            count, fro, to = self.parse_move(move)
            self.move(count, fro, to) 
        
def challenge1():
    board = [
        ['F', 'C', 'P', 'G', 'Q', 'R'],
        ['W', 'T', 'C', 'P'],
        ['B', 'H', 'P', 'M', 'C'],
        ['L', 'T', 'Q', 'S', 'M', 'P', 'R'],
        ['P', 'H', 'J', 'Z', 'V', 'G', 'N'],
        ['D', 'P', 'J'],
        ['L', 'G', 'P', 'Z', 'F', 'J', 'T', 'R'],
        ['N', 'L', 'H', 'C', 'F', 'P', 'T', 'J'],
        ['G', 'V', 'Z', 'Q', 'H', 'T', 'C', 'W']
    ]
    moves = []
    with open("../Input/day5_input.txt") as o:
        for i, line in enumerate(o):
            if i < 10:
                continue
            else:
                moves.append(line.strip())

    cm = CrateMover9000(board, moves)
    cm.simulate_moves()
    for l in cm.board:
        print(l.pop(), end="")
    
def challenge2():
    board = [
        ['F', 'C', 'P', 'G', 'Q', 'R'],
        ['W', 'T', 'C', 'P'],
        ['B', 'H', 'P', 'M', 'C'],
        ['L', 'T', 'Q', 'S', 'M', 'P', 'R'],
        ['P', 'H', 'J', 'Z', 'V', 'G', 'N'],
        ['D', 'P', 'J'],
        ['L', 'G', 'P', 'Z', 'F', 'J', 'T', 'R'],
        ['N', 'L', 'H', 'C', 'F', 'P', 'T', 'J'],
        ['G', 'V', 'Z', 'Q', 'H', 'T', 'C', 'W']
    ]
    moves = []
    with open("../Input/day5_input.txt") as o:
        for i, line in enumerate(o):
            if i < 10:
                continue
            else:
                moves.append(line.strip())

    cm = CrateMover9001(board, moves)
    cm.simulate_moves()
    for l in cm.board:
        if len(l) > 0:
            print(l.pop(), end="")
        else:
            print(' ', end = "")

challenge1()
print()
challenge2()