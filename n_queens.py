def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n, solutions):
    if row == n:
        solutions.append([r.copy() for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"
            solve(board, row + 1, n, solutions)
            board[row][col] = "."


def main():
    n = int(input("Enter value of N: "))
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []

    solve(board, 0, n, solutions)

    print(f"\nTotal Solutions: {len(solutions)}\n")
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}:")
        print_board(solution)


if __name__ == "__main__":
    main()
