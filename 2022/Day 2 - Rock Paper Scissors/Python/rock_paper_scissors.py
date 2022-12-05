class RockPaperScissorsChallenge1:
    def __init__(self):
        self._enum = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
        self.win = ['AZ', 'BX', 'CY']
        self.tie = ['AX', 'BY', 'CZ']
        self.left_score = 0
        self.right_score = 0
    
    def round(self, matchup):
        self.left_score += self._enum[matchup[0]] 
        self.right_score += self._enum[matchup[1]]
        if matchup in self.win:
            self.left_score += 6
            self.right_score += 0
            return 1
        if matchup in self.tie:
            self.left_score += 3
            self.right_score += 3
            return 0
        else:
            self.left_score += 0
            self.right_score += 6
            return -1 

class RockPaperScissorsChallenge2:
    def __init__(self):
        self._enum = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
        self.win = ['AZ', 'BX', 'CY']
        self.tie = ['AX', 'BY', 'CZ']
        self.moves = {
            'X': {'A':'AZ', 'B':'BX', 'C':'CY'},
            'Y': {'A':'AX', 'B':'BY', 'C':'CZ'},
            'Z': {'A':'AY', 'B':'BZ', 'C':'CX'}
        }
        self.left_score = 0
        self.right_score = 0
    
    def round(self, matchup):
        actual_matchup = self.moves[matchup[1]][matchup[0]]
        self.left_score += self._enum[actual_matchup[0]] 
        self.right_score += self._enum[actual_matchup[1]]
        if actual_matchup in self.win:
            self.left_score += 6
            self.right_score += 0
            return 1
        if actual_matchup in self.tie:
            self.left_score += 3
            self.right_score += 3
            return 0
        else:
            self.left_score += 0
            self.right_score += 6
            return -1 

def challenge1():
    rcp = RockPaperScissorsChallenge1()
    with open("../Input/day2_input.txt") as o:
        for line in o:
            matchup = line.strip().replace(' ', '')
            rcp.round(matchup)
        print(f"My score: {rcp.right_score}")


def challenge2():
    rcp = RockPaperScissorsChallenge2()
    with open("../Input/day2_input.txt") as o:
        for line in o:
            matchup = line.strip().replace(' ', '')
            rcp.round(matchup)
        print(f"My score: {rcp.right_score}")


challenge1()
challenge2()