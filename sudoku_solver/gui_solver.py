import tkinter as tk
from tkinter import messagebox

def is_valid(board, num, pos):
    row, col = pos

    for i in range(9):
        if board[row][i] == num and col != i:
            return False
        if board[i][col] == num and row != i:
            return False

    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.entries = [[tk.Entry(root, width=2, font=('Arial', 20), justify='center') for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j, padx=2, pady=2)

        solve_btn = tk.Button(root, text="Solve", command=self.solve_gui, font=('Arial', 14))
        solve_btn.grid(row=9, column=0, columnspan=9, pady=10)

    def solve_gui(self):
        board = []

        try:
            for i in range(9):
                row = []
                for j in range(9):
                    val = self.entries[i][j].get()
                    row.append(int(val) if val else 0)
                board.append(row)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter digits only.")
            return

        if solve(board):
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(board[i][j]))
        else:
            messagebox.showinfo("No Solution", "No solution exists for the given puzzle.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
