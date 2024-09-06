
# Sudoku Solver and Generator

This Python application generates and solves Sudoku puzzles of varying difficulty levels. The app provides functionality to:
- Print Sudoku boards.
- Solve Sudoku puzzles using a backtracking algorithm.
- Validate Sudoku board states based on standard Sudoku rules.

## Features

- **Sudoku Generation**: Generate a Sudoku puzzle with customizable difficulty levels: Very Easy, Easy, Medium, Hard, and Very Hard.
- **Sudoku Solving**: Solve any valid Sudoku puzzle using an efficient backtracking algorithm.
- **Board Printing**: Display Sudoku boards in a human-readable format.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repository/sudoku_generator.git
   cd sudoku_generator
   ```

2. **Install Dependencies**: This app uses Python's built-in libraries, so no additional dependencies are required.

3. **Run the App**:
   ```bash
   python app.py
   ```

## Usage

1. **Generating a Sudoku Puzzle**:
   You can generate a Sudoku board of varying difficulty levels. Modify the `Difficulty` Enum to set the desired difficulty.

2. **Solving a Sudoku Puzzle**:
   You can input an incomplete Sudoku puzzle as a 2D list and call the `solve_sudoku()` function to find a solution.

3. **Printing the Sudoku Board**:
   Use the `print_board()` function to display the Sudoku puzzle in a user-friendly format.

## Example

```python
from app import solve_sudoku, print_board

# Example of an unsolved Sudoku board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

# Solve the board and print the solution
if solve_sudoku(board):
    print_board(board)
else:
    print("No solution exists")
```

## Contributing

Feel free to fork this repository and submit pull requests to improve the app or add new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
