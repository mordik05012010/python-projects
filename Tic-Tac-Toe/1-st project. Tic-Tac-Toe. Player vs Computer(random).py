import random
from colorama import init, Fore, Style

board = [' ' for _ in range(9)]

for row in range(3):
    print(Fore.GREEN + f'| {board[row*3]} | {board[row*3 + 1]} | {board[row*3 + 2]} |')
    if row < 2:
        print('-------------')

current_player = random.choice(['X', 'O'])
game_over = False
turn = 0

while not game_over and turn < 9:
    if current_player == 'X':  # Player
        move = input(f"{Fore.GREEN}Turn {Fore.RED if current_player == 'X' else Fore.BLUE}{current_player}{Fore.GREEN} - Enter a number (1-9): {Style.RESET_ALL}")
        
        if int(move) < 1 or int(move) > 9:
            print(f"{Fore.GREEN}Out of range, enter num (1-9):{Style.RESET_ALL}")
            continue

        move = int(move) - 1

        if board[move] != ' ':
            print(f"{Fore.GREEN}Зайнято. Спробуйте іншу клітинку{Style.RESET_ALL}")
            continue
    else:  
        print(f"{Fore.GREEN}Computer's turn ({current_player})...{Style.RESET_ALL}")
        available_moves = [i for i in range(9) if board[i] == ' ']
        move = random.choice(available_moves)

    board[move] = current_player

    for row in range(3):
        print(f'{Fore.GREEN}| {board[row*3]} | {board[row*3 +1]} | {board[row*3 +2]} |')
        if row < 2:
            print(f'{Fore.GREEN}-------------{Style.RESET_ALL}')

    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal win
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertikal win
        [0, 4, 8], [2, 4, 6]              # Diagonal win
    ]

    for combo in win_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == current_player:
            print(f'{Fore.GREEN}Player {Fore.RED if current_player == "X" else Fore.BLUE}{current_player}{Fore.GREEN} won!{Style.RESET_ALL}')
            game_over = True
            break

    if not game_over:
        current_player = 'O' if current_player == 'X' else 'X'
        turn += 1

if not game_over:
    print(f"{Fore.GREEN}Draw{Style.RESET_ALL}")
