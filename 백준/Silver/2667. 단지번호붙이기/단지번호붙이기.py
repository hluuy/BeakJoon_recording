def dfs(i, j):
    global count
    visited[i][j] = True
    count += 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for p in range(4):
        ni = i + di[p]
        nj = j + dj[p]
        if 0 <= ni < N and 0 <= nj < N:
            if visited[ni][nj] == False and MAP[ni][nj] =='1':
                dfs(ni, nj)

N = int(input())
MAP = [list(input())for _ in range(N)]
visited = [[False] * N for _ in range(N)]
count = 0
result = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and MAP[i][j] == '1':
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()
print(len(result))
for i in result:
    print(i)