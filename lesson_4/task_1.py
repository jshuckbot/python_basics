
def matrix_transpositions(matrix):
    len_matrix = len(matrix)
    len_zero = len(matrix[0])
    tmp_matrix = [[0 for _ in range(len_matrix)] for _ in range(len_zero)]
    
    for i in range(len_matrix):
        for j in range(len_zero):
            tmp_matrix[j][i] = A[i][j]
    print(tmp_matrix)


if __name__ == '__main__':

    A = [[5, 7, 2], [2, 2, 1], [9, 4, 9], [2, 8, 6], [5, 5, 5]]
    matrix_transpositions(A)
