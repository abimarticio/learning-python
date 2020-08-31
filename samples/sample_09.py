# multidimensional lists

matrix = [[1, 2], [3, 4]]
print(matrix)
print(matrix[0][1]) # 2
print(matrix[1][0]) # 3

#[0, 0, 0, 0, 0]
zero_array = [0] * 5
zero_row = [0 for _ in range(5)]
print(zero_array)
print(zero_row)

# ["a"] + ["b"] = ["a", "b"]
# ["*"] * 5 = ["*"] + ["*"] + ["*"] + ["*"] + ["*"]
asterisk_array = ["*"] * 5
# ["*", "*", "*", "*", "*"]
print(asterisk_array)

# make a 5x5 grid
asterisk_matrix = []
for _ in range (5):
    asterisk_matrix.append(asterisk_array)
print(asterisk_matrix)

#equivalently,
asterisk_matrix = [asterisk_array for _ in range(5)]
print(asterisk_matrix)

for row in asterisk_matrix:
    for col in row:
        print(col, end = " ")
    print()


# matrix multiplication
# [2, 2] x [2, 2] = [2, 2] matrix
# [2, 3] x [3, 2] = [2, 2] matrix
# [a, b] x [c, d] = [a, d] matrix

first_row = asterisk_matrix[0]
row_size = len(first_row)
print(row_size)
col_size = len(asterisk_matrix)
print(col_size)


row = [index for index in range (1, 5)]
print(row)
matrix = [row for _ in range(1, 5)]
print(matrix)
for row_index in range(len(matrix)):
    for col_index in range(len(matrix[0])):
        print(matrix[row_index][col_index], end = " ")
    print()

