from flask import Flask, jsonify, request, send_from_directory
import random
import os

app = Flask(__name__)

# ----------------------------
# Sudoku Logic
# ----------------------------
def valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[startRow+i][startCol+j] == num:
                return False
    return True

def solve_board(board):
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
    board = [[0] * 9 for _ in range(9)]
    solve_board(board)
    return board

def remove_numbers(board, attempts=40):
    puzzle = [row[:] for row in board]
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0
        attempts -= 1
    return puzzle

# ----------------------------
# Routes
# ----------------------------
@app.route("/")
def index():
    # serve index.html from same folder
    return send_from_directory(os.path.dirname(__file__), "index.html")

@app.route("/generate", methods=["GET"])
def generate_puzzle():
    solution = generate_full_board()
    puzzle = remove_numbers(solution, attempts=40)
    return jsonify({"puzzle": puzzle, "solution": solution})

@app.route("/solve", methods=["POST"])
def solve_puzzle():
    data = request.json
    board = data["board"]
    solve_board(board)
    return jsonify({"solution": board})

# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)


#http://127.0.0.1:5000