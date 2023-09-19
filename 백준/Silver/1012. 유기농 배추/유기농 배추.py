import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if MAP[ny][nx] == 1:
                MAP[ny][nx] = 0
                dfs(nx, ny)

T = int(input())
for t in range(1, T + 1):
    M, N, K = map(int, sys.stdin.readline().split())
    lst = [list(map(int, sys.stdin.readline().split()))for _ in range(K)]
    MAP = [[0] * M for _ in range(N)]
    count = 0
    for item in lst:
        x, y = item
        MAP[y][x] = 1
    for i in range(M):
        for j in range(N):
            if MAP[j][i] == 1:
                dfs(i, j)
                count += 1
    print(count)