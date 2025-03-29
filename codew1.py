def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)  # Take the first row
        if matrix and matrix[0]:  # Check if matrix is not empty
            for row in matrix:
                result.append(row.pop())  # Take the last column
        if matrix:
            result += matrix.pop()[::-1]  # Take the last row in reverse
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))  # Take the first column
    return result

array = [[1, 2, 3, 5],
         [4, 5, 6, 9],
         [7, 8, 4, 5],
         [5, 7, 8, 9]]

print(*spiral_order(array))
