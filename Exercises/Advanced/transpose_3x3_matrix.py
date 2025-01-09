def transpose(matrix):
    '''
    inputs: matrix (nested lists)
    outputs: matrix (nested lists)

    grab column values and store them in rows.
    column 1 values are row1[0], row2[0], row3[0]
    column 2 values are row1[1], row2[1], row3[1]
    column 3 values are row1[2], row2[2], row3[2]

    
    '''

    columns = range(len(matrix))

    new_matrix = []

    for index in columns:
        new_row = []
        for row in matrix:
            new_row.append(row[index])
        new_matrix.append(new_row)
    
    return new_matrix

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True
