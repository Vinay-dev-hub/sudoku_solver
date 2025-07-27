🧩 Project Title: Sudoku Solver
🎓 SkillCraft Technology – Python Task 03

───────────────────────────────────────────────
📌 Project Description:
This is a Python-based Sudoku Solver that reads a puzzle from a text file, validates it, and solves it using a recursive backtracking algorithm.

It is built using core Python, file input, logic validation, and prints both the unsolved and solved Sudoku grids in the terminal.

───────────────────────────────────────────────
🛠️ Features:
- Solves a standard 9x9 Sudoku puzzle
- Accepts puzzle input from a file (`puzzle.txt`)
- Uses 0 to represent blank cells
- Validates if the input puzzle follows Sudoku rules
- Solves using a recursive backtracking algorithm
- Prints both the original and the solved Sudoku grids

───────────────────────────────────────────────
📁 Project Files:
1. solver.py        → Main Python script to solve Sudoku
2. puzzle.txt       → Input file containing the Sudoku puzzle
3. README.txt       → Project documentation and usage instructions

───────────────────────────────────────────────
▶️ How to Run This Project (macOS + VS Code):

1. Open Terminal
2. Navigate to the folder:
   cd sudoku_solver

3. Make sure `solver.py` and `puzzle.txt` are in the folder

4. Run the solver:
   python3 solver.py

5. You’ll see the unsolved and solved Sudoku printed in the terminal.

───────────────────────────────────────────────
📥 puzzle.txt Format:

- The file must contain 9 lines
- Each line should have 9 numbers (1-9 or 0 for blanks), separated by spaces
- Example:

7 8 0 4 0 0 1 2 0  
6 0 0 0 7 5 0 0 9  
0 0 0 6 0 1 0 7 8  
0 0 7 0 4 0 2 6 0  
0 0 1 0 5 0 9 3 0  
9 0 4 0 6 0 0 0 5  
0 7 0 3 0 0 0 1 2  
1 2 0 0 0 7 4 0 0  
0 4 9 2 0 6 0 0 7  

───────────────────────────────────────────────
✅ Output Example:

Unsolved Sudoku:
7 8 . 4 . . 1 2 .
...

Solved Sudoku:
7 8 5 4 3 9 1 2 6
...

───────────────────────────────────────────────
💻 Built Using:
- Python 3.x
- VS Code on macOS
- No external libraries required

───────────────────────────────────────────────
📦 Optional Enhancements (not required, but useful):
- GUI interface using `tkinter`
- Export solved puzzle to a file
- Accept input from users through GUI or web form
───────────────────────────────────────────────

✨ Submitted by: [Your Name Here]
