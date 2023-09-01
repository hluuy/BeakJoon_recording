def bfs(row, col):
    visited = [[False] * M for _ in range(N)]
    Q = []
    visited[row][col] = True
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    Q.append((row, col))
    while Q:
        i, j = Q.pop(0)
        if i == N - 1 and j == M - 1:
            return visited[i][j]
        for p in range(4):
            ni, nj = i + di[p], j + dj[p]
            if 0 <= ni < N and 0 <= nj < M and MAP[ni][nj] != '0' and visited[ni][nj] == 0:
                Q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1

N, M = map(int,input().split())
MAP = [list(input())for _ in range(N)]

least_move = bfs(0, 0)
print(least_move)