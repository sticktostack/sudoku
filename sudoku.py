import tkinter as tk
import random

# Window setup
root = tk.Tk()
root.title("Sudoku Solver & Generator")
root.geometry("750x700")
root.resizable(False, False)

# Fonts and Colors
ENTRY_FONT = ("Arial", 18, "bold")
BG_COLOR = "#f5f5f5"
BTN_COLOR = "#4CAF50"
BTN_TEXT_COLOR = "white"

root.configure(bg=BG_COLOR)

# ----------------------------
# Sudoku Grid (9x9 Entry Boxes)
# ----------------------------
cells = {}
selected_cell = [None]  # to keep track of which cell is selected
current_puzzle = None   # to store the puzzle
solution_board = None   # to store the solved board

def select_cell(event, row, col):
    """Highlight selected cell and store it"""
    for r in range(9):
        for c in range(9):
            cells[(r, c)].config(bg="white")
    cells[(row, col)].config(bg="#b3d9ff")  # highlight
    selected_cell[0] = (row, col)

def create_grid():
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.place(x=50, y=50)

    for row in range(9):
        for col in range(9):
            e = tk.Entry(frame, width=3, font=ENTRY_FONT,
                         justify="center", relief="ridge", bd=2)
            e.grid(row=row, column=col, padx=(0 if col % 3 else 5, 2),
                   pady=(0 if row % 3 else 5, 2))
            e.bind("<Button-1>", lambda event, r=row, c=col: select_cell(event, r, c))
            cells[(row, col)] = e

create_grid()

# ----------------------------
# Number Buttons (3x3 Keypad)
# ----------------------------
def insert_number(num):
    """Insert number into selected cell"""
    if selected_cell[0] is not None:
        row, col = selected_cell[0]
        cells[(row, col)].delete(0, tk.END)
        cells[(row, col)].insert(0, str(num))

num_frame = tk.Frame(root, bg=BG_COLOR)
num_frame.place(x=600, y=150)

for i in range(1, 10):
    btn = tk.Button(num_frame, text=str(i), width=4, height=2,
                    bg="#2196F3", fg="white", font=("Arial", 12, "bold"),
                    command=lambda x=i: insert_number(x))
    btn.grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)

# ----------------------------
# Sudoku Generator Functions
# ----------------------------
def valid(board, row, col, num):
    """Check if num can be placed"""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    startRow, startCol = 3*(row//3), 3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[startRow+i][startCol+j] == num:
                return False
    return True

def solve_board(board):
    """Backtracking solver"""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if valid(board, row, col, num):
                        board[row][col] = num
                        if solve_board(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_full_board():
    """Generate a complete Sudoku solution"""
    board = [[0]*9 for _ in range(9)]
    solve_board(board)
    return board

def remove_numbers(board, attempts=40):
    """Remove random numbers to create puzzle"""
    puzzle = [row[:] for row in board]
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0
        attempts -= 1
    return puzzle

def display_board(board):
    """Show numbers in grid"""
    for r in range(9):
        for c in range(9):
            cells[(r, c)].delete(0, tk.END)
            if board[r][c] != 0:
                cells[(r, c)].insert(0, str(board[r][c]))
                cells[(r, c)].config(fg="black")  # fixed numbers
            else:
                cells[(r, c)].config(fg="blue")  # empty spots for user

def generate_puzzle():
    """Generate a new Sudoku puzzle"""
    global current_puzzle, solution_board
    solution_board = generate_full_board()
    current_puzzle = remove_numbers(solution_board, attempts=40)
    display_board(current_puzzle)

def solve_puzzle():
    """Solve the current puzzle and display it"""
    global current_puzzle, solution_board
    if current_puzzle is None:
        return
    # Make a copy of the puzzle
    board_copy = [row[:] for row in current_puzzle]
    if solve_board(board_copy):
        display_board(board_copy)

def reset_board():
    """Clear all cells"""
    for r in range(9):
        for c in range(9):
            cells[(r, c)].delete(0, tk.END)

# ----------------------------
# Buttons (Solve, Generate, Reset)
# ----------------------------
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.place(x=150, y=600)

solve_btn = tk.Button(btn_frame, text="Solve", width=12, height=2,
                      bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Arial", 12, "bold"),
                      command=solve_puzzle)
solve_btn.grid(row=0, column=0, padx=10)

generate_btn = tk.Button(btn_frame, text="Generate", width=12, height=2,
                         bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Arial", 12, "bold"),
                         command=generate_puzzle)
generate_btn.grid(row=0, column=1, padx=10)

reset_btn = tk.Button(btn_frame, text="Reset", width=12, height=2,
                      bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Arial", 12, "bold"),
                      command=reset_board)
reset_btn.grid(row=0, column=2, padx=10)

# ----------------------------
# Run the Window
# ----------------------------
root.mainloop()
