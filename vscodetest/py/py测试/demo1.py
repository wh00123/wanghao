import os
import msvcrt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ') 
        print()

def move_player(board, direction):
    player_row, player_col = find_player(board)
    if player_row == -1 and player_col == -1:
        print("未找到玩家角色，无法移动")
        return  # 如果没有找到玩家角色，就不执行移动操作

    if direction == 'w':
        if player_row > 0 and board[player_row-1][player_col] != '#':
            board[player_row][player_col] = ' '
            board[player_row-1][player_col] = 'M'
    elif direction == 's':
        if player_row < len(board)-1 and board[player_row+1][player_col] != '#':
            board[player_row][player_col] = ' '
            board[player_row+1][player_col] = 'M'
    elif direction == 'a':
        if player_col > 0 and board[player_row][player_col-1] != '#':
            board[player_row][player_col] = ' '
            board[player_row][player_col-1] = 'M'
    elif direction == 'd':
        if player_col < len(board[0])-1 and board[player_row][player_col+1] != '#':
            board[player_row][player_col] = ' '
            board[player_row][player_col+1] = 'M'

def find_player(board):
    for row_idx, row in enumerate(board):
        for col_idx, cell in enumerate(row):
            if cell == 'M':
                return row_idx, col_idx
    print("未找到玩家角色")
    return -1, -1  # 返回一个默认坐标

def play_game():
    board = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', 'M', ' ', ' ', ' ', ' ', ' ', ' ', '#'],  # 放置玩家角色'M'
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]

    while True:
        clear_screen()
        print_board(board)

        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')
            move_player(board, key)

play_game()