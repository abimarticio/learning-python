# size: [2, 2] x [2, 2] = [2, 2]
#[[5, 8], [10, 12]] x [[1,2], [9,7]]

# size: [3, 2] X [2, 4] = [3, 4]
# [[3, 4], [2, 5], [4,6]] X [[1, 3, 11, 22], [2, 4, 12, 10]]

a = [[5, 8],
    [10, 12]]
b = [[1,2],
    [9,7]] 
 
# a = [[3, 4],
#     [2, 5],
#     [4,6]] 
# b = [[1, 3, 11, 22],
#     [2, 4, 12, 10]]

c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

for row_index_a in range(len(a)):
    for col in range(len(b[0])):  
        for row_index_b in range(len(b)):
            c[row_index_a][col] += a[row_index_a][row_index_b] * b[row_index_b][col]

print(c)
# [a[0][0] * b[0][0]  +  a[0][1] * b[1][0]         a[0][0] * b[0][1]  +  a[0][1] * b[1][1]]
# [a[1][0] * b[0][0]  +  a[1][1] * b[1][0]         a[1][0] * b[0][1]  +  a[1][1] * b[1][1]]