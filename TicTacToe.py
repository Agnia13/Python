import random
import os
from datetime import datetime

class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'
        self.winner = None
        self.moves_count = 0

    def display(self):
        print('  ' + ' '.join(str(i+1) for i in range(self.size)))
        for i, row in enumerate(self.board):
            print(f"{i+1} " + '|'.join(row))
            if i < self.size - 1:
                print('  ' + '-' * (2 * self.size - 1))

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.moves_count += 1
            return True
        return False

    def check_win(self):
        for row in self.board:
            if all(cell == self.current_player for cell in row):
                return True
        for col in range(self.size):
            if all(self.board[row][col] == self.current_player for row in range(self.size)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(self.size)):
            return True
        if all(self.board[i][self.size - 1 - i] == self.current_player for i in range(self.size)):
            return True
        return False

    def is_draw(self):
        return self.moves_count == self.size * self.size and not self.winner

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_empty_cells(self):
        empty = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == ' ':
                    empty.append((i, j))
        return empty


def save_statistics(game_mode, board_size, first_player, winner, filename='stats/statistics.txt'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"{timestamp} | Режим: {game_mode} | Размер: {board_size} | Первый: {first_player} | Победитель: {winner}\n")


def get_board_size():
    while True:
        try:
            size = int(input("Введите размер игрового поля (>= 3): "))
            if size < 3:
                print("Размер должен быть не меньше 3. Повторите ввод.")
                continue
            return size
        except ValueError:
            print("Некорректный ввод. Введите целое число.")


def get_move_input(game, player_name):
    while True:
        try:
            move = input(f"{player_name} ({game.current_player}), введите строку и столбец (например, 2 3): ").strip().split()
            if len(move) != 2:
                print("Введите два числа через пробел.")
                continue
            row, col = map(int, move)
            if row < 1 or row > game.size or col < 1 or col > game.size:
                print(f"Координаты должны быть от 1 до {game.size}. Повторите.")
                continue
            if not game.make_move(row-1, col-1):
                print("Эта клетка уже занята. Выберите другую.")
                continue
            return True
        except ValueError:
            print("Некорректный ввод. Введите целые числа.")


def ai_move(game):
    empty = game.get_empty_cells()
    return random.choice(empty) if empty else None


def play_game(game_mode, board_size):
    game = TicTacToe(board_size)
    first_player = random.choice(['X', 'O'])
    game.current_player = first_player
    print(f"Первым ходит: {first_player}")

    while True:
        game.display()

        if game_mode == 'human_vs_human':
            player_name = "Игрок 1" if game.current_player == 'X' else "Игрок 2"
            get_move_input(game, player_name)
        else:
            if game.current_player == 'X':
                get_move_input(game, "Вы")
            else:
                print("Робот думает...")
                move = ai_move(game)
                if move:
                    game.make_move(move[0], move[1])

        if game.check_win():
            game.winner = game.current_player
            game.display()
            print(f"Игрок {game.winner} победил!")
            break

        if game.is_draw():
            game.display()
            print("Ничья!")
            game.winner = "Ничья"
            break

        game.switch_player()

    mode_str = "Человек vs Человек" if game_mode == 'human_vs_human' else "Человек vs Робот"
    save_statistics(mode_str, board_size, first_player, game.winner)


def main():
    print("Добро пожаловать в игру «Крестики-нолики»!")
    while True:
        print("\nВыберите режим игры:")
        print("1. Человек против человека")
        print("2. Человек против робота")
        print("3. Выход")
        choice = input("Введите номер (1/2/3): ").strip()

        if choice == '3':
            print("До свидания!")
            break
        if choice not in ['1', '2']:
            print("Неверный выбор. Попробуйте снова.")
            continue

        board_size = get_board_size()
        game_mode = 'human_vs_human' if choice == '1' else 'human_vs_robot'
        play_game(game_mode, board_size)

        again = input("Сыграем ещё? (y/n): ").strip().lower()
        if again != 'y':
            print("До свидания!")
            break


main()
