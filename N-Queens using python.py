def is_safe(pane, rows, column, N):
    for i in range(column):
        if pane[i] == rows or \
           pane[i] - i == rows - column or \
           pane[i] + i == rows + column:
            return False
    return True

def solve_n_queens1(pane, column, N):
    if column >= N:
        return True

    for i in range(N):
        if is_safe(pane, i, column, N):
            pane[column] = i
            if solve_n_queens1(pane, column + 1, N):
                return True
    return False

def solve_n_queens(N):
    pane = [-1] * N
    if not solve_n_queens1(pane, 0, N):
        print("Solution does not exist.")
        return

    for i in range(N):
        rows_str = ""
        for j in range(N):
            if pane[j] == i:
                rows_str += "Q "
            else:
                rows_str += "0 "
        print(rows_str.strip())

N = int(input("Enter the value of N: "))
solve_n_queens(N)


