MAP = [list(map(int, input().split()))for _ in range(9)]
max_v = 0
for i in range(9):
    for j in range(9):
        a = MAP[i][j]
        if max_v < a:
            max_v = a
        if max_v == MAP[i][j]:
            row, col = i+1, j+1
print(max_v)
print(row, col)