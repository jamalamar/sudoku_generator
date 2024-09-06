import random
from enum import Enum
from typing import List, Tuple

class Difficulty(Enum):
    VERY_EASY = "very easy"
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    VERY_HARD = "very hard"

def print_board(board: List[List[int]]) -> None:
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(board: List[List[int]], row: int, col: int, num: int) -> bool:
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board: List[List[int]]) -> bool:
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                random_nums = list(range(1, 10))
                random.shuffle(random_nums)
                for num in random_nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku() -> List[List[int]]:
    board = [[0] * 9 for _ in range(9)]
    fill_board(board)
    return board

def fill_board(board: List[List[int]], row: int = 0, col: int = 0) -> bool:
    # Move to the next cell
    if row == 9:
        return True  # Finished filling the board
    if col == 9:
        return fill_board(board, row + 1, 0)  # Move to the next row

    if board[row][col] != 0:
        return fill_board(board, row, col + 1)  # Skip filled cells

    numbers = list(range(1, 10))
    random.shuffle(numbers)

    for num in numbers:
        if is_valid(board, row, col, num):
            board[row][col] = num
            if fill_board(board, row, col + 1):  # Move to the next cell
                return True
            board[row][col] = 0  # Backtrack

    return False  # Trigger backtracking to the previous cell



def get_cells_to_remove(difficulty: Difficulty) -> int:
    return {
        Difficulty.VERY_EASY: random.randint(30, 34),
        Difficulty.EASY: random.randint(36, 40),
        Difficulty.MEDIUM: random.randint(41, 45),
        Difficulty.HARD: random.randint(46, 50),
        Difficulty.VERY_HARD: random.randint(51, 54)
    }[difficulty]

def remove_numbers(board: List[List[int]], difficulty: Difficulty) -> None:
    cells_to_remove = get_cells_to_remove(difficulty)
    count = 0
    while count < cells_to_remove:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != 0:
            backup = board[row][col]
            board[row][col] = 0
            if not has_unique_solution(board):
                board[row][col] = backup
            else:
                count += 1

def has_unique_solution(board: List[List[int]]) -> bool:
    # Placeholder for actual implementation.
    return True  # Assume there's a function that reliably checks for this.

def generate_multiple_sudoku(num_boards: int, difficulty: Difficulty) -> List[List[List[int]]]:
    boards = []
    for _ in range(num_boards):
        board = generate_sudoku()
        remove_numbers(board, difficulty)
        boards.append(board)
    return boards


def main() -> None:
    print("Welcome to the Sudoku Generator!")

    number_of_boards = int(input("How many Sudoku boards would you like to generate? "))
    while number_of_boards <= 0:
        print("Please enter a positive integer.")
        number_of_boards = int(input("How many Sudoku boards would you like to generate? "))
    
    difficulty_level = input("Select difficulty (very easy, easy, medium, hard, very hard): ").lower()
    while difficulty_level not in Difficulty._value2member_map_:
        print("Invalid input. Please choose a valid difficulty level.")
        difficulty_level = input("Select difficulty (very easy, easy, medium, hard, very hard): ").lower()
    
    sudoku_boards = generate_multiple_sudoku(number_of_boards, Difficulty[difficulty_level.upper()])
    for idx, board in enumerate(sudoku_boards):
        print(f"Sudoku Board {idx + 1}:")
        print_board(board)
        print()

if __name__ == "__main__":
    main()
