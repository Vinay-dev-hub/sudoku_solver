def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(grid, num, pos):
    row, col = pos

    # Row check
    if num in grid[row]:
        return False

    # Column check
    if num in [grid[i][col] for i in range(9)]:
        return False

    # 3x3 Box check
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False

    return True

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True  # Solved

    row, col = find

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0  # Backtrack

    return False

def load_from_file(filename):
    with open(filename, "r") as f:
        board = []
        for line in f:
            row = list(map(int, line.strip().split()))
            if len(row) != 9:
                raise ValueError("Each line must have 9 numbers")
            board.append(row)
        if len(board) != 9:
            raise ValueError("There must be 9 rows")
        return board

def validate_puzzle(board):
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                board[i][j] = 0
                if not is_valid(board, num, (i, j)):
                    return False
                board[i][j] = num
    return True

if __name__ == "__main__":
    try:
        sudoku_board = load_from_file("puzzle.txt")

        print("Unsolved Sudoku:\n")
        print_grid(sudoku_board)

        if not validate_puzzle(sudoku_board):
            print("\n❌ Invalid Sudoku puzzle. It breaks Sudoku rules.")
        elif solve(sudoku_board):
            print("\n✅ Solved Sudoku:\n")
            print_grid(sudoku_board)
        else:
            print("\n❌ No solution exists.")
    except Exception as e:
        print("⚠️ Error:", e)
