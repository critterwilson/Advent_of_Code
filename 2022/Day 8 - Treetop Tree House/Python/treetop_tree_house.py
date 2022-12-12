def is_visible(input:list, col:int, row:int, total_col:int, total_row:int):
    current_tree_value = int(input[row][col])
    # left
    left = max([int(input[row][i]) for i in range(0, col)])
    # right
    right = max([int(input[row][i]) for i in range(col+1, total_col)])
    # up
    up = max([int(input[i][col]) for i in range(0, row)])
    # down
    down = max([int(input[i][col]) for i in range(row+1, total_row)])
    if current_tree_value > left or current_tree_value > right or current_tree_value > up or current_tree_value > down:
        return True
    else:
        return False

def visibility_distance(input:list, col:int, row:int, total_col:int, total_row:int):
    current_tree_value = int(input[row][col])
    # left
    left_dist = 0
    left = [int(input[row][i]) for i in range(col-1, -1, -1)]
    if left:
        for x in left:
            left_dist += 1
            if x >= current_tree_value:
                break
    # right
    right_dist = 0
    right = [int(input[row][i]) for i in range(col+1, total_col)]
    if right:
        for x in right:
            right_dist += 1
            if x >= current_tree_value:
                break
    
    # up
    up_dist = 0
    up = [int(input[i][col]) for i in range(row - 1, -1, -1)]
    if up:
        for x in up:
            up_dist += 1
            if x >= current_tree_value:
                break
    # down
    down_dist = 0
    down = [int(input[i][col]) for i in range(row+1, total_row)]
    if down:
        for x in down:
            down_dist += 1
            if x >= current_tree_value:
                break

    return up_dist*down_dist*left_dist*right_dist

def test():
    input = [x.strip() for x in open("../Input/test_input.txt").readlines()]
    rows = len(input)
    cols = len(input[0])
    total_visible = 2 * (rows + cols) - 4
    for x in range(1, cols - 1):
        for y in range(1, rows - 1):
            if is_visible(input, y, x, cols, rows):
                total_visible += 1

    print(total_visible)

def challenge1():
    input = [x.strip() for x in open("../Input/day8_input.txt").readlines()]
    rows = len(input)
    cols = len(input[0])
    total_visible = 2 * (rows + cols) - 4
    for x in range(1, cols - 1):
        for y in range(1, rows - 1):
            if is_visible(input, y, x, cols, rows):
                total_visible += 1

    print(total_visible)

def challenge2():
    input = [x.strip() for x in open("../Input/day8_input.txt").readlines()]
    rows = len(input)
    cols = len(input[0])
    vis = [[0 for _ in range(cols)] for _ in range(rows)]
    for x in range(cols):
        for y in range(rows):
            vis[x][y] = visibility_distance(input, y, x, cols, rows)
    
    print(max([max(x) for x in vis]))


test()
challenge1()
challenge2()