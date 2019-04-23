"""
Write an algorithm such that if an element in an NxN matrix is 0, its entire
row and column are set to 0.
"""
# def zero_matrix(matrix: list):
#     "Naive, takes O(N^2) space and O(N^3) time"
#     zeroed = {}
#     for r, row in enumerate(matrix):
#         for c, value in enumerate(row):
#             if (r, c) not in zeroed and value == 0:
#                 # row
#                 for c2, _ in enumerate(row):
#                     zeroed[(r, c2)] = True
#                     row[c2] = 0

#                 # column
#                 for r2, row2 in enumerate(matrix):
#                     zeroed[(r2, c)] = True
#                     row2[c] = 0

def zero_matrix(matrix: list):
    """Optimal, takes O(1) space and O(N^2) time."""
    row_has_zero = False
    col_has_zero = False

    # Check if the first row has a zero
    for c in matrix[0]:
        if c == 0:
            row_has_zero = True
            break

    # Check if the first col has a zero
    for r in matrix:
        if r[0] == 0:
            col_has_zero = True
            break
    
    # Check for zeros in the rest of the array
    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[0])):
            if c == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    # Nullify rows based on values in first column
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)

    # Nullify columns based on values in first row
    for j in range(1, len(matrix)):
        if matrix[0][j] == 0:
            nullify_column(matrix, j)

    # Nullify first row
    if row_has_zero:
        nullify_row(matrix, 0)

    # Nullify first col
    if col_has_zero:
        nullify_column(matrix, 0)

def nullify_column(matrix: list, col: int):
    for row in matrix:
        row[col] = 0

def nullify_row(matrix: list, row: int):
    for i in range(len(matrix)):
        matrix[row][i] = 0
