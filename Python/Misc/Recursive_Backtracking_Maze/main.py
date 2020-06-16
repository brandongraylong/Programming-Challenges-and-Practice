import time


STEP_SYMBOL = '@'
WALL_SYMBOL = '|'
PATH_SYMBOL = '.'

def valid_move(maze: list, c_row: int, c_col: int, num_rows: int, num_cols: int) -> bool:
    if c_row < 0 or c_row > num_rows:
        return False
    if c_col < 0 or c_col > num_cols:
        return False
    if maze[c_row][c_col] == WALL_SYMBOL:
        return False
    if maze[c_row][c_col] == STEP_SYMBOL:
        return False
    return True

def at_end(c_row: int, c_col: int, end_row: int, end_col: int) -> bool:
    if c_row == end_row and c_col == end_col:
        return True
    return False

def solve(maze: list, start: list, end: list) -> bool:
    maze[start[0]][start[1]] = STEP_SYMBOL

    for i in range(len(maze)):
        print(maze[i])
    print()
    time.sleep(1)

    if at_end(start[0], start[1], end[0], end[1]):
        return True

    if valid_move(maze, start[0]-1, start[1], end[0], end[1]):
        maze[start[0]-1][start[1]] = STEP_SYMBOL
        if solve(maze, [start[0]-1, start[1]], end):
            return True
        maze[start[0]-1][start[1]] = PATH_SYMBOL

    if valid_move(maze, start[0]+1, start[1], end[0], end[1]):
        maze[start[0]+1][start[1]] = STEP_SYMBOL
        if solve(maze, [start[0]+1, start[1]], end):
            return True
        maze[start[0]+1][start[1]] = PATH_SYMBOL

    if valid_move(maze, start[0], start[1]-1, end[0], end[1]):
        maze[start[0]][start[1]-1] = STEP_SYMBOL
        if solve(maze, [start[0], start[1]-1], end):
            return True
        maze[start[0]][start[1]-1] = PATH_SYMBOL

    if valid_move(maze, start[0], start[1]+1, end[0], end[1]):
        maze[start[0]][start[1]+1] = STEP_SYMBOL
        if solve(maze, [start[0], start[1]+1], end):
            return True
        maze[start[0]][start[1]+1] = PATH_SYMBOL

    return False

def main():
    maze = [['.', '.', '.'],
            ['.', '|', '|'],
            ['.', '.', '|'],
            ['.', '|', '.'],
            ['.', '.', '|'],
            ['|', '.', '.'],
            ['.', '.', '|'],
            ['.', '.', '.']]
    print('INITIAL:')
    for i in range(len(maze)):
        print(maze[i])
    print()

    print('LIVE LOOK:')
    solved = solve(maze, [0, 0], [len(maze)-1, len(maze[-1:][0])-1])
    print()

    print('RESULT: solved=' + str(solved))
    for i in range(len(maze)):
        print(maze[i])
    print()

if __name__ == '__main__':
    main()
