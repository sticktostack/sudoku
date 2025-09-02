import tkinter as tk

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
            e.grid(row=row, column=col, padx=(0 if col % 3 else 5, 2), pady=(0 if row % 3 else 5, 2))
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

# Create 3x3 grid for numbers 1-9
for i in range(1, 10):
    btn = tk.Button(num_frame, text=str(i), width=4, height=2,
                    bg="#2196F3", fg="white", font=("Arial", 12, "bold"),
                    command=lambda x=i: insert_number(x))
    btn.grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)

# ----------------------------
# Buttons (Solve, Generate, Reset)
# ----------------------------
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.place(x=150, y=600)

solve_btn = tk.Button(btn_frame, text="Solve", width=12, height=2,
                      bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Arial", 12, "bold"))
solve_btn.grid(row=0, column=0, padx=10)

generate_btn = tk.Button(btn_frame, text="Generate", width=12, height=2,
                         bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Arial", 12, "bold"))
generate_btn.grid(row=0, column=1, padx=10)

reset_btn = tk.Button(btn_frame, text="Reset", width=12, height=2,
                      bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Arial", 12, "bold"))
reset_btn.grid(row=0, column=2, padx=10)

# ----------------------------
# Run the Window
# ----------------------------
root.mainloop()

