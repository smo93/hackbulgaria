def magic_square(matrix):
    magic_sum = sum(matrix[0])
    transposed = [list(x) for x in zip(*matrix)]
    d1 = [matrix[i][i] for i in range(len(matrix))]
    d2 = [transposed[i][i] for i in range(len(transposed))]
    if sum(d1) != magic_sum and sum(d2) != magic_sum:
        return False
    for row in range(len(matrix)):
        if sum(matrix[row]) != magic_sum or sum(matrix[row]) != magic_sum:
            return False
    return True
