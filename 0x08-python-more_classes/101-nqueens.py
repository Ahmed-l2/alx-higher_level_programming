#!/usr/bin/python3
import sys
""" N-Queens Puzzle"""


def is_integer(value):
    """
    Check if a given value is an integer.

    Args:
        value (str): The value to check.

    Returns:
        bool: True if the value is an integer, False otherwise.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def solve_nqueens(N):
    """
    Solve the N Queens problem and print solutions.

    Args:
        N (str): The size of the chessboard and the number of queens.

    Raises:
        ValueError: If N is not a valid integer.
        SystemExit: If the input conditions are not met (N is not a valid
        integer, or N is less than 4).

    Returns:
        None
    """
    def is_safe(board, row, col):
        """
        Check if it's safe to place a queen at a specific position on the
        board.

        Args:
            board (list): The current state of the chessboard.
            row (int): The row to check.
            col (int): The column to check.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        for i in range(row):
            if board[i][1] == col or \
               board[i][1] - i == col - row or \
               board[i][1] + i == col + row:
                return False
        return True

    def place_queen(board, row):
        """
        Recursively place queens on the chessboard.

        Args:
            board (list): The current state of the chessboard.
            row (int): The current row to place a queen.

        Returns:
            None
        """
        if row == N:
            print_solution(board)
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = [row, col]
                place_queen(board, row + 1)

    def print_solution(board):
        """
        Print the solution in the specified format.

        Args:
            board (list): The final state of the chessboard.

        Returns:
            None
        """
        print(board)

    if not is_integer(N):
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[-1, -1] for _ in range(N)]

    place_queen(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
