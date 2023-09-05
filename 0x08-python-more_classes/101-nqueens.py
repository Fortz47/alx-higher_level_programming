#!/usr/bin/python3
"""A module doc"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at the given row and column.

    Args:
        board (list of list): The N×N chessboard.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(n):
    """
    Solve the N-Queens problem and print all possible solutions.

    Args:
        n (int): The size of the chessboard.

    Prints:
        All possible solutions to the N-Queens problem, one solution per line.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve_util(board, col):
        if col >= n:
            solutions.append([row[:] for row in board])
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve_util(board, col + 1)
                board[i][col] = 0

    solve_util(board, 0)

    if not solutions:
        print("No solution exists")
        sys.exit(1)

    for solution in solutions:
        print_solution(solution)


def print_solution(board):
    """
    Print a single solution to the N-Queens problem.

    Args:
        board (list of list): The N×N chessboard representing a solution.
    """
    queens = []
    for row in board:
        for col, cell in enumerate(row):
            if cell == 1:
                queens.append([board.index(row), col])
    print(queens)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)
