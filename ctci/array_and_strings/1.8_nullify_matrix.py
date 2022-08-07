def zero_matrix(matrix):
    """
    O(n*m) time O(n*m)
    """
    n = len(matrix)
    m = len(matrix[0])
    found_zero = []
    
    #Define a function to clear all rows and column depend on the given indices.
    def set_zero(i,j):
        for col in range(n):
            matrix[col][j] = 0
        for row in range(m):
            matrix[i][row] = 0
        
    #Find and insert a set of indices when zero is found.
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                found_zero.append((i,j))
    #loop over the indices of zero and call the function to clear its rows and columns.
    for i, j in found_zero:
        set_zero(i,j)
    return matrix


def zero_matrix2(matrix):
    """
    O(nm) Time O(1) space as we use the matrix itself. We use the first row and column
    of the matrix has markers for what needs the be clears. We first check whether the
    first row or column has 0 so we can handle it later.
    """
    def nullify_rows(row):
        for i in range(m):
            matrix[row][i] = 0
        
    def nullify_columns(col):
        for i in range(n):
            matrix[i][col] = 0

    n = len(matrix)
    m = len(matrix[0])
    first_row_has_zero = False
    first_col_has_zero = False

    for i in range(n):
        if matrix[i][0] == 0:
            first_col_has_zero = True
    for i in range(m):
        if matrix[0][i] == 0:
            first_row_has_zero = True

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[0][j] = 0 
                matrix[i][0] = 0

    for i in range(1,n):
        if matrix[i][0] == 0:
            nullify_rows(i)

    for i in range(1,m):
        if matrix[0][i] == 0:
            nullify_columns(i)

    if first_row_has_zero:
        nullify_rows(0)
    if first_col_has_zero:
        nullify_columns(0)

    return matrix


x = [
    [1,2,0,9,12],
    [4,3,1,5,11],
    [1,4,0,6,10]
    ]

y = zero_matrix2(x)
for i in range(len(y)):
    print(y[i])